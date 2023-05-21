import argparse
import execptions
from .commandList import commands, commandSchema

class ArgumentParser:
    
    has_instance = False    
    argumentParser : argparse.ArgumentParser = None
    
    def __init__(self) -> None:
        raise execptions.SingleTonException()
    
    
    @classmethod
    def initArgumentParser() -> argparse.ArgumentParser:
        if not ArgumentParser.has_instance and not ArgumentParser.argumentParser:
            ArgumentParser.argumentParser = argparse.ArgumentParser(prog="PortScanner!",
                                                                description="simple port scanner cli app",
                                                                epilog="All Rights Reserved @ RzxKhn")
            ArgumentParser.has_instance = True
            ArgumentParser.mountCommands()
    
    
    @classmethod
    def mountCommands() -> bool:
        for i in commands:
            res = commandSchema.validate(i)
            if not res :
                raise execptions.CommandSchemaIncorrect
        for i in commands:
            ArgumentParser.argumentParser.add_argument(i['command_name'],type=i["type"],help=i["help"])
        
        ArgumentParser.argumentParser.parse_args()
    
    
    
        
        

    