from ..execptions import SingleTonException
import argparse
class ArgumentParser:
    has_instance = False    
    argumentParser : argparse.ArgumentParser = None
    def __init__(self) -> None:
        raise SingleTonException()
    
    
    @classmethod
    def getArgumentParser() -> argparse.ArgumentParser:
        ArgumentParser.argumentParser = argparse.ArgumentParser()
        ArgumentParser.has_instance = True
        
    

    