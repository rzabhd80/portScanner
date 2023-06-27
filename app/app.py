import threading
import datetime
import multiprocessing
import core.commandParser as Command_parser
import argparse


def app():
    Command_parser.ArgumentParser.init_argument_parser()


if __name__ == "__main__":
    app()
