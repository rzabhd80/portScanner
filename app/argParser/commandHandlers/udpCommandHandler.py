import datetime
import socket
import threading
import core.commandHandler as command_handler
from collections.abc import Sequence
import argparse
from typing import Any
import argparse


class UdpScannerCommandHandler(command_handler.CommandHandler):


    def __check_udp_connection(self, ip: str, port: int) -> bool:
        try:
            udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp_socket.settimeout(1)
            test_message = b"Test"
            udp_socket.sendto(test_message, (ip, port))
            response, _ = udp_socket.recvfrom(1024)
            udp_socket.close()
            return True

        except (socket.timeout, ConnectionRefusedError, ConnectionResetError):
            print(ConnectionResetError)
            return False

    def __udp_port_scanner_in_port_range(self, from_port: int, to_port: int, ip: str):
        result = [self.__check_udp_connection(ip, i) for i in range(from_port, to_port)]
        map(lambda x: print(x), [i for i in result])

    def __udp_scanner_init_thread(self, ip: str, from_port: int, until_port: int) -> list:
        num_ports = until_port - from_port
        num_threads = 4
        ports_per_thread = num_ports // num_threads

        threads = []
        for i in range(num_threads):
            start_port = (i * ports_per_thread) + from_port
            end_port = ports_per_thread + start_port
            thread = threading.Thread(target=self.__udp_port_scanner_in_port_range, args=(start_port, end_port, ip))
            threads.append(thread)
        return threads

    def handle(self, ip: str, from_port: int, until_port: int):
        threads = self.__udp_scanner_init_thread(ip, from_port, until_port)
        print("Starting Threads")
        start_time = datetime.datetime.now()
        [thread.start() for thread in threads]
        [thread.join() for thread in threads]
        stop_time = datetime.datetime.now()
        time_difference = stop_time - start_time
        time_difference_seconds = time_difference.total_seconds()
        print("This action took : ", time_difference_seconds, " seconds !")
        print("Done")
