import socket


def check_tcp_connection(ip, port):
    try:
        # Create a TCP socket
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout for the socket
        tcp_socket.settimeout(1)  # Adjust the timeout value as needed

        # Attempt to establish a TCP connection
        tcp_socket.connect((ip, port))

        # Close the socket
        tcp_socket.close()

        return True

    except (socket.timeout, ConnectionRefusedError, ConnectionResetError):
        return False
