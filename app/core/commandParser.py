import argparse

import execptions as exception
import argParser.commandList as commandList


class ArgumentParser:
    has_instance = False
    argumentParser: argparse.ArgumentParser = None

    def __init__(self) -> None:
        raise exception.SingleTonException()

    @classmethod
    def init_argument_parser(cls) -> argparse.ArgumentParser:
        if not ArgumentParser.has_instance and not ArgumentParser.argumentParser:
            ArgumentParser.argumentParser = argparse.ArgumentParser(prog="PortScanner!",
                                                                    description="simple port scanner cli app",
                                                                    epilog="All Rights Reserved @ RzxKhn")
            ArgumentParser.has_instance = True
            return ArgumentParser.mount_commands()

    @classmethod
    def mount_commands(cls) -> argparse.ArgumentParser.parse_args:
        commandList.init_commands(ArgumentParser.argumentParser)        
        args = ArgumentParser.argumentParser.parse_args()
        return args
