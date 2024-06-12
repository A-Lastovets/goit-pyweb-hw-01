import colorama
from colorama import Fore
colorama.init(autoreset=True)
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self): str
    pass

class Close(Command):
    def execute(self) -> str:
        return Fore.GREEN + "Good bye!"
    
class Hello(Command):
    def execute(self) -> str:
        return Fore.GREEN + "How can I help you?\n"

class Help(Command):
    def execute(self) -> str:
        return f'''{Fore.YELLOW}
 If you want to add new contact --->\t\t\t\t please enter : 'name' + 'phone'\t\t\tNOTE: phone must be 10 digits\n \
If you want to add birthday ---> \t\t\t\t please enter : 'add-birthday' + 'name' + 'birth date' \
\tNOTE: birth date must be in format 'DD.MM.YYYY'\n \
If you want to review all contacts ---> \t\t\t please enter : 'all'\t\t\t\t\t\n \
If you want to review upcoming birthdays for next 7 days ---> \t please enter : 'birthdays'\t\t\t\t\n \
If you want to change contact's phone ---> \t\t\t please enter : 'change' + 'name' + 'old phone' + 'new phone'\t\n \
If you want to delete the contact ---> \t\t\t please enter : 'delete' + 'name'\t\t\t\t\n \
If you want to delete the phone users ---> \t\t\t please enter : 'delete-phone' + 'name' + 'phone number'\t\t\t\t\n \
If you want to review the contact's phone ---> \t\t please enter : 'phone' + 'name'\t\t\t\t\n \
If you want to review the birthday of any user ---> \t\t please enter : 'show-birthday' + 'name'\t\t\t\n \
If you want to shut down the assistant bot ---> \t\t please enter : 'close' or 'exit'\t\t\t\n
'''
    
class WrongCommand(Command):
    def execute(self):
        return Fore.RED + "Invalid command, please try again. \nIf you want to exit the bot : type 'exit' or 'close'\n "

class Add_contact(Command):
    def __init__(self, args, book) -> None:
        self.book = book
        self.args = args

    def execute(self) -> str:
        return f"{self.add_contact(self.args)}\n"

class Delete_contact(Command):
    def __init__(self, args, book) -> None:
        self.book = book
        self.args = args

    def execute(self):
        return f"{self.book.delete_contact(self.args)}\n"

class Delete_phone(Command):
    def __init__(self, args, book) -> None:
        self.book = book
        self.args = args

    def execute(self):
        return f"{self.book.delete_phone(self.args)}\n"

class Change_phone(Command):
    def __init__(self, *args, book) -> None:
        self.book = book
        self.args = args

    def execute(self):
        return f"{self.book.change_phone(self.args)}\n"

class Show_phone(Command):
    def __init__(self, args, book) -> None:
        self.book = book
        self.args = args

    def execute(self):
        return self.book.show_phone(self.args)

class Show_all(Command):
    def __init__(self, args, book) -> None:
        self.book = book
        self.args = args

    def execute(self):
        return self.book.show_all(self.args)

class Add_Birthday(Command):
    def __init__(self, args, book) -> None:
        self.book = book
        self.args = args

    def execute(self):
        name, date = self.args
        return f"{self.book.add_birthday(name, date)}\n"

class Show_Birthday(Command):
    def __init__(self, args, book) -> None:
        self.book = book
        self.args = args

    def execute(self):
        return f"{self.book.show_birthday(self.args)}\n"

class Birthdays(Command):
    def __init__(self, book) -> None:
        self.book = book

    def execute(self):
        return f"{self.book.get_upcoming_birthdays()}\n"