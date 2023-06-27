from collections.abc import Sequence
import datetime
import socket
import threading
import core.commandHandler as command_handler


class TcpScannerCommandHandler(command_handler.CommandHandler):

    def __check_tcp_connection(self, ip: str, port: int) -> bool:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.settimeout(1)
        res = tcp_socket.connect_ex((ip, port)) 
        tcp_socket.close()
        return True if res == 0 else False

    def __tcp_port_scanner_in_port_range(self, from_port: int, to_port: int, ip: str):
        port_list = [i for i in range(from_port, to_port + 1)]
        result = [self.__check_tcp_connection(ip, i) for i in port_list]
        result_of_port = list(zip(port_list, result))
        [print(f"port {i[0]} is open") if i[1] is True else print(f"port {i[0]} is closed") for i in result_of_port]

    def __tcp_scanner_init_thread(self, ip: str, from_port: int, until_port: int) -> list:
        num_ports = (until_port - from_port) + 1
        num_threads = 4
        ports_per_thread = num_ports // num_threads

        threads = []
        for i in range(num_threads):
            start_port = (i * ports_per_thread) + from_port
            end_port = ports_per_thread + start_port
            thread = threading.Thread(target=self.__tcp_port_scanner_in_port_range, args=(start_port, end_port, ip))
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
