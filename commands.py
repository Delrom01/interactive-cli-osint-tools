"""
Fichier de code définissant les commandes du CLI

Romain Delalande
"""
import subprocess
from colorama import Fore

WAIT_MESSAGE = f"{Fore.YELLOW} Veuillez patienter {Fore.RESET} \n"


class Commands:
    """
    Classe définissant toutes les commandes du CLI
    """

    def __init__(self) -> None:
        """
        Fonction permettant de définir et d'initialiser les instances
        ("variables globales au CLI") utiles dans les fonctions suivantes

        """
        print(f"{Fore.YELLOW} --- Initialisation des instances nécessaires --- {Fore.RESET} \n")

    def __del__(self) -> None:
        """
        Fonction permettant de supprimer proprement les instances

        """
        print(f"{Fore.YELLOW} --- Suppression des instances --- {Fore.RESET}")

    def exit(self):
        """
        Fonction permettant de quitter le CLI

        """

    def reset_instances(self):
        """
        Fonction permettant de réinitialiser les instances de la classe

        """
        print(f"{Fore.YELLOW} DEMARRAGE DU PROGRAMME DE RESET DES INSTANCES... {Fore.RESET}")
        print("")
        self.__init__()
        print("")
        print(f"{Fore.YELLOW} FIN DU PROGRAMME DE RESET DES INSTANCES {Fore.RESET}")

    def toutatis(self, sessionsid: str, username: str) -> None:
        """
        Toutatis est un outil qui vous permet d'extraire des informations des comptes
        instagrams tels que les e-mails, les numéros de téléphone et plus encore

        Args:
            sessionsid (str): id de session instagram (cookies)
            username (str): username (pseudo) du compte instagram à OSINT

        """
        print(f"{Fore.YELLOW} DEMARRAGE DU PROGRAMME TOUTATIS... {Fore.RESET}")
        print("")
        print(WAIT_MESSAGE)

        try:
            toutatis = subprocess.Popen(f"toutatis -s {sessionsid} -u {username}",
                                        shell=True, stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE, universal_newlines=True)
            out_toutatis, err_toutatis = toutatis.communicate()
            toutatis.wait()
            print(out_toutatis)

        except KeyboardInterrupt:
            print(f"{Fore.RED} Interruption utilisateur {Fore.RESET}")

        print(f"{Fore.YELLOW} FIN DU PROGRAMME TOUTATIS {Fore.RESET}")

    def ignorant(self, country_code: int, phone: int) -> None:
        """
        Ignorant est un outil qui vous permet de vérifier si un numéro de téléphone
        est utilisé sur différents sites comme snapchat, instagram et plus encore

        Args:
            country_code (int): code téléphonique du pays (ex: +33)
            phone (int): numéro de téléphone (9 chiffres)

        """
        print(f"{Fore.YELLOW} DEMARRAGE DU PROGRAMME IGNORANT... {Fore.RESET}")
        print("")
        print(WAIT_MESSAGE)

        try:
            ignorant = subprocess.Popen(f"ignorant {country_code} {phone}",
                                        shell=True, stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE, universal_newlines=True)
            out_ignorant, err_ignorant = ignorant.communicate()
            ignorant.wait()
            print(out_ignorant)

        except KeyboardInterrupt:
            print(f"{Fore.RED} Interruption utilisateur {Fore.RESET}")

        print(f"{Fore.YELLOW} FIN DU PROGRAMME IGNORANT {Fore.RESET}")
