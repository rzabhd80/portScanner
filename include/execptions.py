class SingleTonException(Exception):
    def __init__(self) -> None:
        super().__init__("singleTon can not be instantiated")
        
