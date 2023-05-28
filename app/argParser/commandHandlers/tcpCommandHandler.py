from argparse import ArgumentParser, Namespace
from collections.abc import Sequence
import datetime
import socket
import threading
from typing import Any
import core.commandHandler as command_handler
import argparse

class TcpScannerCommandHandler(command_handler.CommandHandler,argparse.Action):
    
    
    def __call__(self, parser: ArgumentParser, namespace: Namespace, 
                 values: str | Sequence[Any] | None, option_string: str | None = None) -> None:
        
        ip = namespace.ip    
        ports = self.__get_ports()
        self.handle(ip=ip,from_port=ports[0],until_port=ports[1])
        return super().__call__(parser, namespace, values, option_string)
    
    
    def __get_ports(parser : Namespace):
        ports = parser.ports
        list_of_ports = []
        for i in ports:
            if "-" in ports:
                starting_port,ending_port = map(int,ports.split("-"))
                list_of_ports.append( x for x in range(starting_port,ending_port+1))
            else :
               raise Exception("")
                
        return list_of_ports
    
    def __check_tcp_connection(self, ip: str, port: int) -> bool:
        try:
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_socket.settimeout(1)
            tcp_socket.connect((ip, port))
            tcp_socket.close()
            return True
        except (socket.timeout, ConnectionRefusedError, ConnectionResetError):
            return False

    def __tcp_port_scanner_in_port_range(self, from_port: int, to_port: int, ip: str):
        result = [self.__check_tcp_connection(ip, i) for i in range(from_port, to_port)]
        map(lambda x: print(x), [i for i in result])

    def __tcp_scanner_init_thread(self, ip: str, from_port: int, until_port: int) -> list:
        num_ports = until_port - from_port
        num_threads = 4
        ports_per_thread = num_ports // num_threads

        threads = []
        for i in range(num_threads):
            start_port = (i * ports_per_thread) + from_port
            end_port = ports_per_thread + start_port
            thread = threading.Thread(target=self.__tcp_port_scanner_in_port_range, args=(start_port, end_port,ip))
            threads.append(thread)
        return threads

    def handle(self, ip: str, from_port: int, until_port: int):
        threads = self.__tcp_scanner_init_thread(ip, from_port, until_port)
        print("Starting Threads")
        start_time = datetime.datetime.now()
        [thread.start() for thread in threads]
        [thread.join() for thread in threads]
        stop_time = datetime.datetime.now()
        time_difference = stop_time - start_time
        time_difference_seconds = time_difference.total_seconds()
        print("This action took : ", time_difference_seconds, " seconds !")
        print("Done")
