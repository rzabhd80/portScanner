from ..argParseer.commandList import commands
import argparse


class CommandExecutor:
    def __int__(self):
        raise Exception()

    @classmethod
    def execute_command(cls, arg_parser: argparse.ArgumentParser):
        for i in commands:
            if arg_parser.i["command_name"]:
                i['commandHandler']()
