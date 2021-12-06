"""
Fichier de code définissant les commandes du CLI
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
        Function allowing to set and initialise the instances
        ("global variables") useful in the following functions

        """
        print(f"{Fore.YELLOW} --- Initialisation of the necessary instances --- {Fore.RESET} \n")

    def __del__(self) -> None:
        """
        Function to cleanly delete instances

        """
        print(f"{Fore.YELLOW} --- Deletion of instances --- {Fore.RESET}")

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
        Toutatis is a tool that allows you to extract information from
        instagrams accounts such as e-mails, phone numbers and more

        Args:
            sessionsid (str): instagram sessionid (in cookies)
            username (str): username of the instagram profile to OSINT

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
        Toutatis is a tool that allows you to check if a phone number
        is used on different sites like snapchat, instagram and more

        Args:
            country_code (int): country telephone code
            phone (int): phone number (9 digits)

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
