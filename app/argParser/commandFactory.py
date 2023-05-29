import argparse
from argparse import ArgumentParser, Namespace
from collections.abc import Sequence
from typing import Any
import argParser.commandHandlers.tcpCommandHandler as tcpHandler
import argParser.commandHandlers.udpCommandHandler as udpHandler
import execptions as customExceptions


class CommandFactory(argparse.Action):

    def __call__(self, parser: ArgumentParser, namespace: Namespace, values: str | Sequence[Any] | None,
                 option_string: str | None = None) -> None:
        ports = CommandFactory.__get_ports(parser=namespace)
        tcp_scanner = tcpHandler.TcpScannerCommandHandler()
        udp_scanner = udpHandler.UdpScannerCommandHandler()
        udp_scanner.handle(from_port=ports[0], until_port=ports[1],
                           ip=namespace.ip) if namespace.protocol == "udp" else tcp_scanner.handle(from_port=ports[0],
                                                                                                   until_port=ports[1],
                                                                                                   ip=namespace.ip)

    @classmethod
    def __get_ports(cls, parser: Namespace):
        ports = parser.ports
        list_of_ports =  list(map(int, ports[0].split("-")))
        list(list_of_ports)    
        return list_of_ports
