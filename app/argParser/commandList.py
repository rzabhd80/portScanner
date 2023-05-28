import argparse


def init_commands(parser: argparse.ArgumentParser):
    parser.add_argument("ip", type=str, help="ip of the server to be scanned")
    parser.add_argument("--protocol", dest="protocol", type=str, choices=["tcp", "udp"], default="tcp")
    parser.add_argument("--ports", dest="ports",nargs="+", type=str,required=True)
