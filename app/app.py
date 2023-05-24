import udpchecker
import tcpchecker
import threading
import datetime
import multiprocessing
from argParseer.commandParser import ArgumentParser



def app():    
    ArgumentParser.initArgumentParser()
    
    from_port = 1000
    until_port = 65002
    num_ports = until_port - from_port
    num_threads = 4
    ports_per_thread = num_ports // num_threads

    threads = []
    for i in range(num_threads):
        start_port = (i * ports_per_thread) + from_port
        end_port = ports_per_thread + start_port
        # thread = threading.Thread(target=tcp_port_scanner, args=(start_port, end_port))
        thread = threading.Thread(target=tcp_port_scanner, args=(start_port, end_port))
        threads.append(thread)

    print("Starting Threads")
    start_time = datetime.datetime.now()

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    print("arg parser")

    stop_time = datetime.datetime.now()
    time_difference = stop_time - start_time
    time_difference_seconds = time_difference.total_seconds()
    print("This action took : ", time_difference_seconds, " seconds !");
    print("Done")


def tcp_port_scanner(start_from, end_port):
    ip = "127.0.0.1"
    for i in range(start_from, end_port):
        # result = udpchecker.check_udp_connection(ip, i)
        result = tcpchecker.check_tcp_connection(ip, i)
        if result:
            print(i, result)


if __name__ == "__main__":
    app()
