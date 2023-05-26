from schema import Schema, Optional, Use
import core.commandHandler as command_handler
# from .commandHandlers.tcpCommandHandler import TcpScannerCommandHandler
import argParser.commandHandlers.udpCommandHandler as Udp_command_handler
import argParser.commandHandlers.tcpCommandHandler as Tcp_command_handler

commands = [
    {'command_name': 'ip', 'type': int, 'help': 'ip of the server to be scanned',
     'nargs': '+'},

    {'command_name': '--tcp', 'type': str, 'help': 'TCP scanning',
     'commandHandler': Tcp_command_handler.TcpScannerCommandHandler},

    {'command_name': '--udp', 'type': str, 'help': 'UDP scanning',
     'commandHandler': Udp_command_handler.UdpScannerCommandHandler},

    {'command_name': '--port-range', 'type': int, 'help': 'port range to be scanned',
     'nargs': '+'}
]
