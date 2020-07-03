from xmlrpc.client import boolean
from random import randint

from reptile import Reptile

class Snake(Reptile):  # subclass of Reptile
    forked_tongue = boolean()
    venom = boolean()
    limb = boolean()
    prey_list = ["frog",
                 "rat",
                 "toad",
                 "mouse",
                 "rabbit",
                 "wolf"]  # List of possible prey encounters
    target = {"Prey": "",
              "Alive": False
              }  # Dictionary

    def __init__(self):  # Override init in Reptile Class
        super().__init__()
        self.forked_tongue = True
        self.tetrapod = False
        self.limb = True
        self.heart_cambers = 3

    def hunt(self):  # Snakes use their tongue to smell...
        # Pick random prey from list and generate random number to select prey
        self.target["Prey"] = self.prey_list[randint(0, (len(self.prey_list) - 1))]
        self.target["Alive"] = True
        print("You see a " + self.target["Prey"] + ", what will you do? \n [Attack] or [Constrict] or [Poison]")
        return