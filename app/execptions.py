class SingleTonException(Exception):
    def __init__(self) -> None:
        super().__init__("singleTon can not be instantiated")


class CommandSchemaIncorrect(Exception):
    def __init__(self) -> None:
        super().__init__('command schema is not correct')


class IncorrectPortRangeError(Exception):
    def __init__(self) -> None:
        super().__init__("given port range schema is incorrect")
