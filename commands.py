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
        """
        Toutatis is a tool that allows you to extract information from instagrams accounts such as e-mails, phone numbers and more

        Args:
            username: username of the instagram profile to OSINT
            sessionsId: instagram sessionid (in cookies)

        Returns: nothing

        """
        core.main(username, sessionsId)


    def exit(self):  # function to leave the cli
        pass
