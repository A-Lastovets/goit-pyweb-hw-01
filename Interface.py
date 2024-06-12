from abc import ABC, abstractmethod


class Interface(ABC):
    @abstractmethod
    def entering(self, text):
        pass

    @abstractmethod
    def printing(self, text):
        pass


class CommandLine(Interface):

    def entering(self, text):
        return input(f'{text}')

    def printing(self, text):
        print(text)