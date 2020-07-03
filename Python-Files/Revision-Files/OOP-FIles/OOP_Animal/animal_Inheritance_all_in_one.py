# This file demonstrates the concept of Inheritance.
# Inheritance is when you define a new class with little to no modifications to an existing class.
# The new class is called derived(or child) class and the one from which it inherits
# is called the base (or parent) class.

# ~ Exercise ~
# Create classes and inherit from each as shown in the diagram in Day14_Training.md
# The exercise is to define 4 classes: Animal, Reptile, Snake and Python - then to implement
# inheritance through the classes
# Depending on the class that is being made, for example a Python which is a species of snake is not venomous, therefore
# it could set the venom variable to false.
from xmlrpc.client import boolean
from random import randint


class Animal:
    alive = boolean()  # Class attribute - boolean() sets the alive status to false by default
    spine = True
    eyes = True
    lungs = True

    # If there is something be set in this init then it is a instance_attribute unique to that instance of the class
    def __init__(self):
        self.alive = True  # This sets the alive variable to True when an instance of this or child classes are made
        pass

    def hunt(self):
        pass

    def eat(self):
        pass

    def procreate(self):
        pass

    def move(self):
        pass


# If you had another class in a different file from this you would import it like this:
# from 'folder_name' import 'class_name'
# These classes are in the same file therefore they do not need to be imported.
# In this structure the Animal is the parent class it is inherited by Reptile, which is inherited by Snake
# and that is further inherited by the Python class.

class Reptile(Animal):  # Subclass of Animal class
    cold_blooded = boolean()
    tetrapod = boolean()  # four limbs
    heart_cambers = [3, 4]  # Crocodiles have 4 heart chambers, all other reptiles have 3
    amniotic_eggs = boolean()  # eggs with membrane to protect baby

    def __init__(self):  # Override original init in parent class
        super().__init__()
        self.amniotic_eggs = True
        self.cold_blooded = True

    def seek_heat(self):
        if type(self).__name__ == "Reptile":
            return "Please choose a more specific type of reptile first!"

    def attack(self):
        pass

    def poison(self):
        pass

    def attract_mate_through_scent(self):
        pass


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


class Python(Snake):  # subclass of Snake
    Large = boolean()
    two_lungs = boolean()

    def __init__(self):  # Override init in Snake Class
        super().__init__()
        self.Large = True
        self.two_lungs = True
        self.venom = True

    def eat(self):  # Overrides the eat method in the Animal class, to perform unique functionality
        if self.target["Prey"] == "":  # They snake has no prey at the moment.
            print("You haven't currently got any prey")
        else:
            if not self.target["Alive"]:
                print("Nom nom nom... The dead " + self.target["Prey"] + " was delightful!")
                self.target["Prey"] = ""  # Sets prey back to None E.G. Removes the prey
                self.target["Alive"] = False
            else:
                print("The " + self.target["Prey"] + " is not dead")

    def constrict(self):
        if self.target["Prey"] == "toad" or self.target["Prey"] == "rabbit":
            print("You killed it!")
            self.target["Alive"] = False
        else:
            print("The target is too strong!")

    def poison(self):
        if self.target["Prey"] == "wolf":
            print("You killed it!")
            self.target["Alive"] = False
        else:
            print("The target is too strong!")

    def attack(self):
        if self.target["Prey"] == "frog" or self.target["Prey"] == "rat" or self.target["Prey"] == "mouse":
            print("You killed it!")
            self.target["Alive"] = False
        else:
            print("The target is too strong!")

    @staticmethod
    def climb():
        return "You climb up high!"

    @staticmethod
    def shed_skin():
        return "you shed your skin... look at you!"


Rocky_the_python = Python()
print(Rocky_the_python.hunt())
print(Rocky_the_python.attack())

