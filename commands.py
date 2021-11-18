import time

from colorama import *

# for holehe
from holehe.modules.social_media.snapchat import snapchat
import httpx

init()  # for colorama


class Instances:  ######!! This file contains all the commands that can be used/launched with the cli !!######

    def __init__(
            self) -> None:  # function allowing to set and initialise the instances ("global variables") useful in the following functions
        print(Fore.YELLOW + """--- Initialisation of the necessary instances ---""" + Fore.RESET)
        # declaration of the instances on the model :
        # self.var_1 = value_1     (value_1 is int, float, bool ...)
        # self.var_2 = value_2     (value_2 is int, float, bool ...)

    def __del__(self) -> None:  # function to cleanly delete instances
        print(Fore.YELLOW + """--- Deletion of instances ---""" + Fore.RESET)

    '''
    def function_1(self, param_1, param_2) -> None:  # function with 2 parameters in entry
        """
        Args:
            param_1: Description of the parameter param_1
            param_2: Description of the parameter param_2
        Returns:
            #if return something
        """
        ###
        # code of the function_1
        # you can use the parameters in the following way (for exemple) :
        # print(param_1)
        ###
    '''

    async def holehe(self, email):  # function to checks if an email is attached to an account on sites like twitter, instagram, imgur and more than 120 others

        # email = input("Saisir une adresse mail :")
        print(email)
        out = []
        client = httpx.AsyncClient()

        await snapchat(email, client, out)
        # time.sleep(5)

        print(out)
        await client.aclose()



    def exit(self):  # function to leave the cli
        pass