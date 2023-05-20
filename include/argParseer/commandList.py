from schema import Schema

commandSchema = Schema({'command_name':str,'type':int | str, 'help' : str})

commands  = [
    {'command_name' : 'ip', 'type' : str,'help':'ip of the server to be scanned'}
]