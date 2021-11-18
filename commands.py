from colorama import *

# for toutatis
from toutatis import core

init()  # for colorama


class Instances:  ######!! This file contains all the commands that can be used/launched with the cli !!######

    def __init__(
            self) -> None:  # function allowing to set and initialise the instances ("global variables") useful in the following functions
        print(Fore.YELLOW + """--- Initialisation of the necessary instances ---""" + Fore.RESET)

    def __del__(self) -> None:  # function to cleanly delete instances
        print(Fore.YELLOW + """--- Deletion of instances ---""" + Fore.RESET)

    def toutatis(self, username, sessionsId):
        resultat = core.main(username, sessionsId)
        print(resultat)

    def exit(self):  # function to leave the cli
        pass
