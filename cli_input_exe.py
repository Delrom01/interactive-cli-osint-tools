"""
Fichier de code du CLI par saisie des commandes au clavier.


Utilisation du CLI :

    -  Une liste des commandes disponibles est affichée et la sélection
       se fait par saisie du nom de la commande au clavier.

    -  Un système d'autocomplétion est disponible à l'aide de la touche <Tab>.

"""
import inspect
import commands  # commands.py file
from colorama import Fore
import questionary


class ExceptionExit(Exception):
    """
    Exception qui permet de quitter le CLI.

    """


def cli(commands_object):
    """
    Fonction qui génère l'interface CLI par saisie des commandes au clavier.

    Args:
            commands_object : fichier de commandes à partir duquel générer l'interface.

    """
    # récupération de la liste des fonctions (des commandes) du fichier commands.py
    commands_list = []
    search_commands = inspect.getmembers(commands_object, inspect.ismethod)
    for command in search_commands:
        if not command[0].startswith("_"):
            commands_list.append(command[0])

    # affichage de la liste des commandes récupérées
    print("Liste des commandes disponibles : ")
    for cmd in commands_list:
        print(f"*  {cmd}")
    print("")

    # sélection de la commande à exécuter par l'utilisateur
    choice = questionary.autocomplete("Quelle commande voulez-vous exécuter ?",
                                      choices=commands_list).ask()

    # boucle en cas de saisie correspondant à aucune commande (erreur de saisie)
    while choice not in commands_list:
        print(f"{Fore.YELLOW} La commande entry est incorrecte {Fore.RESET}")
        print("")
        choice = questionary.autocomplete("Quelle commande voulez-vous exécuter ?",
                                          choices=commands_list).ask()

    # si la fonction "exit" est sélectionnée : levée d'exception
    if choice == "exit":
        raise ExceptionExit

    # suppression des arguments self de la liste des arguments
    params = inspect.getfullargspec(getattr(commands_object, choice))
    args_fct = params.args[:]
    del args_fct[args_fct.index("self")]

    # si fonction sans argument, appel direct
    if not args_fct:
        print("")
        getattr(commands_object, choice)()
        print("")

    # si fonction avec arguments, saisie des arguments avant appel de fonction
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

    print(f"\n{Fore.YELLOW} --- DEBUT DU PROGRAMME --- {Fore.RESET}")
    # initialisation de l'objet de la classe Commands (commands.py)
    # permet de garder la modification de potentielles variables jusqu'à la fermeture du CLI
    # (ou de la réinitialisation des instances)
    commands_objt = commands.Commands()

    # boucle permettant le CLI interactif
    USER_INPUT = True
    while USER_INPUT:
        try:
            cli(commands_objt)
        except ExceptionExit:
            USER_INPUT = not questionary.confirm("Êtes-vous sûr de vouloir quitter ?").ask()
            print("\n")

    commands_objt.exit()
    print(f"{Fore.YELLOW} --- FIN DU PROGRAMME --- {Fore.RESET}")
