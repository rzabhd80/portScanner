import core.commandHandler as commandHandler
import socket,threading,datetime
class TcpScannerCommandHandler(commandHandler.CommandHandler):
    def __check_tcp_connection(self,ip:str,port:str) -> None:
         try:
           tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           tcp_socket.settimeout(1)  
           tcp_socket.connect((ip, port))
           tcp_socket.close()
           return True
         except (socket.timeout, ConnectionRefusedError, ConnectionResetError):
           return False
    
    def __tcp_scanner(self,from_port:str,until_port:str)->None:
        num_ports = until_port - from_port
        num_threads = 4
        ports_per_thread = num_ports // num_threads

        threads = []
        for i in range(num_threads):
           start_port = (i * ports_per_thread) + from_port
           end_port = ports_per_thread + start_port
           thread = threading.Thread(target=self.tcp_port_scanner, args=(start_port, end_port))
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
        
       
    def handle(slef):
        return super().handle()