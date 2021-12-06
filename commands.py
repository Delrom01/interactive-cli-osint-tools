"""
Fichier de code définissant les commandes du CLI

Romain Delalande
"""
import subprocess
import questionary
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
        print(f"{Fore.YELLOW} DEMARRAGE DU PROGRAMME TOUTATIS... {Fore.RESET}\n")
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
        display = questionary.select("Voulez-vous afficher uniquement les sites trouvés ou tous les résultats ? ",
                                     choices=("Only used", "All")).ask()
        print(f"\n{Fore.YELLOW} DEMARRAGE DU PROGRAMME IGNORANT... {Fore.RESET}\n")
        print(WAIT_MESSAGE)

        try:
            if "Only used" in display:
                ignorant = subprocess.Popen(f"ignorant --only-used {country_code} {phone}",
                                            shell=True, stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE, universal_newlines=True)
                out_ignorant, err_ignorant = ignorant.communicate()
                ignorant.wait()
                print(out_ignorant)

            else:
                ignorant = subprocess.Popen(f"ignorant {country_code} {phone}",
                                            shell=True, stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE, universal_newlines=True)
                out_ignorant, err_ignorant = ignorant.communicate()
                ignorant.wait()
                print(out_ignorant)

        except KeyboardInterrupt:
            print(f"{Fore.RED} Interruption utilisateur {Fore.RESET}")

        print(f"{Fore.YELLOW} FIN DU PROGRAMME IGNORANT {Fore.RESET}")

    def holehe(self, email: str) -> None:
        """
        Holehe vérifie si un mail est attaché à un compte sur des sites
        comme twitter, instagram, imgur et plus de 120 autres

        Args:
            email (int): adresse mail à vérifier (ex: test@gmail.com)

        """
        display = questionary.select("Voulez-vous afficher uniquement les sites trouvés ou tous les résultats ? ",
                                choices=("Only used", "All")).ask()
        print(f"\n{Fore.YELLOW} DEMARRAGE DU PROGRAMME HOLEHE... {Fore.RESET}\n")
        print(WAIT_MESSAGE)
        try:
            if "Only used" in display:
                holehe = subprocess.Popen(f"holehe --only-used {email}",
                                            shell=True, stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE, universal_newlines=True)
                out_holehe, err_holehe = holehe.communicate()
                holehe.wait()
                print(out_holehe)

            else:
                holehe = subprocess.Popen(f"holehe {email}",
                                          shell=True, stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE, universal_newlines=True)
                out_holehe, err_holehe = holehe.communicate()
                holehe.wait()
                print(out_holehe)

        except KeyboardInterrupt:
            print(f"{Fore.RED} Interruption utilisateur {Fore.RESET}")

        print(f"{Fore.YELLOW} FIN DU PROGRAMME HOLEHE {Fore.RESET}")
