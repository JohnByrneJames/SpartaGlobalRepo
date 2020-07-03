from xmlrpc.client import boolean

from animal import Animal

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


cracker = Reptile()

print(cracker.procreate())
