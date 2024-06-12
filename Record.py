from datetime import datetime
import colorama
from colorama import Fore
colorama.init(autoreset=True)

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError(Fore.RED + "Invalid date format. Use DD.MM.YYYY")

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError(Fore.RED + "Phone number must be 10 digits.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
        phones_list_str = [str(phone) for phone in self.phones]

        if phone_number in phones_list_str:
            raise ValueError(Fore.YELLOW + "Phone is alredy in the list")

        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        self.phones = [p for p in self.phones if str(p) != phone_number]
        
    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
        print(Fore.YELLOW + "Phone number not found.")

    def find_phone(self, phone):
        for number in self.phones:
            if number.value == phone:
                return phone
        
        return Fore.YELLOW + f"Phone {phone} is not in the list"

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        return Fore.BLUE + f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}, birthday: {self.birthday}"