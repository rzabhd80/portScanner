from collections.abc import Sequence
import datetime
import socket
import threading
import core.commandHandler as command_handler
from contextlib import closing

class TcpScannerCommandHandler(command_handler.CommandHandler):

    def __check_tcp_connection(self, ip: str, port: int) -> bool:
         with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
             sock.settimeout(1)
             return True if  sock.connect_ex((ip,port)) == 0 else False

    def __tcp_port_scanner_in_port_range(self, from_port: int, to_port: int, ip: str):
        port_list = [i for i in range(from_port, to_port + 1)]
        result = [self.__check_tcp_connection(ip, i) for i in port_list]
        result_of_port = list(zip(port_list, result))
        [print(f"port {i[0]} is open") if i[1] is True else print(f"port {i[0]} is closed") for i in result_of_port]

    def __tcp_scanner_init_thread(self, ip: str, from_port: int, until_port: int) -> list:
        
        threads = []
        all_ports = [i for i in range(from_port,until_port+1)]
        threads = []
        [threads.append(threading.Thread(target=self.__tcp_port_scanner_in_port_range, args=(i, i, ip))) for i in all_ports]
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
