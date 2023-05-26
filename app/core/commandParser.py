import argparse

from ..execptions import CommandSchemaIncorrect, SingleTonException
from ..argParseer import commandList


class ArgumentParser:
    has_instance = False
    argumentParser: argparse.ArgumentParser = None

    def __init__(self) -> None:
        raise SingleTonException()

    @classmethod
    def init_argument_parser(cls) -> argparse.ArgumentParser:
        if not ArgumentParser.has_instance and not ArgumentParser.argumentParser:
            ArgumentParser.argumentParser = argparse.ArgumentParser(prog="PortScanner!",
                                                                    description="simple port scanner cli app",
                                                                    epilog="All Rights Reserved @ RzxKhn")
            ArgumentParser.has_instance = True
            ArgumentParser.mount_commands()
            return ArgumentParser.argumentParser

    @classmethod
    def mount_commands(cls) -> None:
        for i in commandList.commands:
            res = commandList.commandSchema.validate(i)
            if not res:
                raise CommandSchemaIncorrect
        for i in commandList.commands:
            ArgumentParser.argumentParser.add_argument(i['command_name'], type=i["type"],
                                                       nargs='+', help=i["help"])
        ArgumentParser.argumentParser.parse_args()

