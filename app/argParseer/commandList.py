from schema import Schema, Optional
from ..core.commandHandler import CommandHandler
from .commandHandlers.tcpCommandHandler import TcpScannerCommandHandler

commandSchema = Schema(
    {'command_name': str, 'type': int | str, 'help': str, Optional('commandHandler'):
        CommandHandler, Optional('nargs')
     :str})

commands = [
    {'command_name': 'tcp-scanner', 'type': str, 'help': 'ip of the server to be scanned',
     'commandHandler': TcpScannerCommandHandler},

    {'command_name': '--port-range', 'type': int, 'help': 'port range to be scanned',
     'nargs': '+'}
]
