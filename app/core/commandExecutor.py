#from ..argParser.commandList import commands
import argParser.commandList as commandList
import argparse
import argParser.commandHandlers.tcpCommandHandler as tcpHandler
import argParser.commandHandlers.udpCommandHandler as udpHandler


class CommandExecutor:
    def __int__(self):
        raise Exception()
    
    
    @classmethod
    def __commandFactory(cls,protocol : str)-> None:
        if protocol == "tcp":
            return tcpHandler.TcpScannerCommandHandler()
        else :
            return udpHandler.UdpScannerCommandHandler.handle()

    @classmethod
    def execute_command(cls, arg_parser: argparse.Namespace):
        ip = arg_parser.ip
        protocol = arg_parser.protocol
        ports = arg_parser.ports
        list_of_ports = []
        for i in ports:
            if "-" in ports:
                starting_port,ending_port = map(int,ports.split("-"))
                list_of_ports.append( x for x in range(starting_port,ending_port+1))
            else :
                list_of_ports.append(int(ports))
                