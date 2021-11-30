from colorama import *

from tools.toutatis.toutatis import core_toutatis
from tools.ignorant.ignorant import core_ignorant

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
        core_toutatis.main(username, sessionsId)

    def ignorant(self, country_code, phone):
        """

        Args:
            country_code: country telephone code
            phone: phone number (9 digits)

        Returns: nothing

        """
        core_ignorant.main(country_code, phone)

    def exit(self):  # function to leave the cli
        pass
