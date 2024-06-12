from datetime import datetime
import colorama
from colorama import Fore
colorama.init(autoreset=True)
import time
from AddressBook import *
import Command as cmd 
from Record import *
from file import *
from Interface import CommandLine

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

interface = CommandLine()

def main():
    book = load_data()
    now = datetime.now()
    current_date = datetime.today().date()
    current_time = now.strftime("%H:%M")
    interface.printing(Fore.GREEN + f">>>Welcome to the assistant bot!<<<")
    interface.printing(f"Today is : {current_date} \nTime : {current_time}")
    interface.printing("\033[3m{}".format("\n>>>If you don't know how to start your work, please check the help information by typing the command 'help'<<<\n"))

    while True:
        user_input = interface.entering("Enter a command: ")
        if not user_input: 
            interface.entering("Please enter a command.")
            continue
        command, *args = parse_input(user_input)
        match command:
            case "close" | "exit":
                out = cmd.Close()
                interface.printing(out.execute())
                time.sleep(2)
                save_data(book)
                break
            case "hello":         out = cmd.Hello()
            case "add":           out = cmd.Add_contact(args, book)
            case "change":        out = cmd.Change_phone(*args, book)
            case "phone":         out = cmd.Show_phone(args, book)
            case "all":           out = cmd.Show_all(book)
            case "add-birthday":  out = cmd.Add_Birthday(args, book)
            case "show-birthday": out = cmd.Show_Birthday(args, book)
            case "birthdays":     out = cmd.Birthdays(args, book)
            case "delete":        out = cmd.Delete_contact(args, book)
            case "delete-phone":  out = cmd.Delete_phone(args, book)
            case "help":          out = cmd.Help()
            case _:               out = cmd.WrongCommand()
        interface.printing(out.execute())

if __name__ == "__main__":
    main()