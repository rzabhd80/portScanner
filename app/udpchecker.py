import socket


def check_udp_connection(ip, port):
    try:
        # Create a UDP socket
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Set a timeout for the socket
        udp_socket.settimeout(1)  # Adjust the timeout value as needed

        # Send a test message to the IP address and port
        test_message = b"Test"
        udp_socket.sendto(test_message, (ip, port))

        # Attempt to receive a response
        response, _ = udp_socket.recvfrom(1024)

        # If a response is received, the connection is successful
        udp_socket.close()
        return True

    except (socket.timeout, ConnectionRefusedError, ConnectionResetError):
        print(ConnectionResetError)
        return False
