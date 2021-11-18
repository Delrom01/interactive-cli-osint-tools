import questionary
import inspect
import commands    #commands.py file
from colorama import *

import trio

init()   #for colorama


def cli():                  ######!! cli with a list of functions to be selected by arrows !!######
    commands_list = []
    search_commands = inspect.getmembers(commands.Instances, inspect.isfunction)  # commands = commands.py file
    for i in range(len(search_commands)):
        if search_commands[i][0] == "__del__":
            pass
        else:
            commands_list.append(search_commands[i][0])

    choice = questionary.select("Which command do you want to run ?", choices=commands_list).ask()

    if choice == "exit":
        exit = questionary.confirm("Do you want to cancel 'exit' ?").ask()
        print("")
        return choice, exit

    else:
        args = []
        params = inspect.getfullargspec(getattr(commands.Instances, choice))
        for arg in params.args:
            if arg == "self":
                pass
            else:
                args.append(arg)

        if not args:
            print("")
            getattr(Instance, choice)()
            print("")
        else:
            doc = inspect.getdoc(getattr(commands.Instances, choice))
            print("")
            print("usage : commands.py [OPTION] COMMAND [ARGS]...")
            print("")
            print(doc)
            print("")
            args_values = [""]
            for i in range(len(args)):
                entry = questionary.text(f"Enter a value for the argument {args[i]} : ").ask()
                args_values.append(entry)
            print("")
            getattr(commands.Instances, choice)(*args_values)
            print("")

        exit = questionary.confirm("Do you want to enter a new command ?").ask()
        print("")
        return choice, exit


if __name__ == "__main__":
    print(Fore.YELLOW + """--- START OF PROGRAM ---""" + Fore.RESET)
    Instance = commands.Instances()
    print("")
    entry = cli()
    while entry[1] == True:
        entry = cli()
    del Instance
    print(Fore.YELLOW + """--- END OF PROGRAM ---""" + Fore.RESET)
