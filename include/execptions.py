class SingleTonException(Exception):
    def __init__(self,message : str, error : str) -> None:
        super().__init__(message)