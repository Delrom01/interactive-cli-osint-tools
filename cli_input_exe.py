"""
Fichier de code du CLI de saisie des commandes au clavier
"""
import inspect
import commands  # commands.py file
import questionary
from colorama import Fore


class ExceptionExit(Exception):
    """
    Exception qui permet de quitter le CLI

    """


def cli(commands_object):  # cli with a list of functions to be selected by input keyboard
    """
    Fonction qui génère l'interface CLI

    """
    commands_list = []
    search_commands = inspect.getmembers(commands_object, inspect.ismethod)
    for command in search_commands:
        if not command[0].startswith("_"):
            commands_list.append(command[0])

    print("Liste des commandes disponibles : ")
    for cmd in commands_list:
        print(f"*  {cmd}")
    print("")

    choice = questionary.autocomplete("Quelle commande voulez-vous exécuter ?",
                                      choices=commands_list).ask()

    while choice not in commands_list:
        print(f"{Fore.YELLOW} La commande entry est incorrecte {Fore.RESET}")
        print("")
        choice = questionary.autocomplete("Quelle commande voulez-vous exécuter ?",
                                          choices=commands_list).ask()

    if choice == "exit":
        raise ExceptionExit

    # suppression des arguments self
    params = inspect.getfullargspec(getattr(commands_object, choice))
    args_fct = params.args[:]
    del args_fct[args_fct.index("self")]

    # si fonction sans argument, appel direct
    if not args_fct:
        print("")
        getattr(commands_object, choice)()
        print("")

    # si fonction avec arguments, saisie avant appel
    else:
        doc = inspect.getdoc(getattr(commands_object, choice))
        print("\n")
        print(doc)
        print("\n")
        args_values = []
        for arg in args_fct:
            user_entry = questionary.text(
                f"Saisir une valeur pour l'argument {arg} : ").ask()
            args_values.append(user_entry)
        print("\n")
        getattr(commands_object, choice)(*args_values)
        print("\n")


if __name__ == "__main__":

    print(f"\n{Fore.YELLOW} --- START OF PROGRAM --- {Fore.RESET}")
    commands_objt = commands.Commands()

    user_input = True
    while user_input:
        try:
            cli(commands_objt)
        except ExceptionExit:
            user_input = not questionary.confirm("Êtes-vous sûr de vouloir quitter ?").ask()
            print("\n")
    commands_objt.exit()
    print(f"{Fore.YELLOW} --- FIN DU PROGRAMME --- {Fore.RESET}")
