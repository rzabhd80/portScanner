#from ..argParser.commandList import commands
import argParser.commandList as commandList
import argparse


class CommandExecutor:
    def __int__(self):
        raise Exception()

    @classmethod
    def execute_command(cls, arg_parser: argparse.ArgumentParser):
        [i['commandHandler']() for i in commandList.commands if
         arg_parser.i['commandHandler'] is not None
         and i['commandHandler']]
