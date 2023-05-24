from schema import Schema
import core.commandHandler as commandHandler

commandSchema = Schema({'command_name':str,'type':int | str, 'help' : str,'commandHandler' : commandHandler.CommandHandler})

commands  = [
    {'command_name' : 'ip', 'type' : str,'help':'ip of the server to be scanned'}
]