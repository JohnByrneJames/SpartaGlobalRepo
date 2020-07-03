from xmlrpc.client import boolean

from snake import Snake

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
print(Rocky_the_python.eat())