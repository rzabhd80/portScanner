from ..execptions import SingleTonException

class ArgumentParser:
    has_instance = False    
    
    def __init__(self) -> None:
        raise SingleTonException()
    

    