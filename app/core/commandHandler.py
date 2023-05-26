from abc import ABC, abstractmethod


class CommandHandler(ABC):
    @abstractmethod
    def handle(self, *args, **kwargs):
        pass
