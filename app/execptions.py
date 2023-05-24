class SingleTonException(Exception):
    def __init__(self) -> None:
        super().__init__("singleTon can not be instantiated")
        
class CommandSchemaIncorrect(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__('command schema is not correct')