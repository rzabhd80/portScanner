from schema import Schema
from ..core.commandHandler import CommandHandler
from .commandHandlers.tcpCommandHandler import TcpScannerCommandHandler

commandSchema = Schema(
    {'command_name': str, 'type': int | str, 'help': str, 'commandHandler': CommandHandler})

commands = [
    {'command_name': 'ip', 'type': str, 'help': 'ip of the server to be scanned',
     'commandHandler': TcpScannerCommandHandler()}
]
