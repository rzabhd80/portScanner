import argparse

import argParser.commandHandlers.tcpCommandHandler as tcpHandler
import argParser.commandHandlers.udpCommandHandler as udHandler
import argParser.commandFactory as commandFactory


def init_commands(parser: argparse.ArgumentParser):
    parser.add_argument("ip", type=str, help="ip of the server to be scanned")
    parser.add_argument("--ports", nargs="+", dest="ports", type=str, help="ports or range of ports", required=True)
    parser.add_argument("--protocol", dest="protocol", choices=["tcp", "udp"], type=str, required=True)
    parser.add_argument("--action", dest="action", type=str, action=commandFactory.CommandFactory, required=True,
                        choices=["run"])
