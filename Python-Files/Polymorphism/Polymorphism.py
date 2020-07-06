# Polymorphism

# Polymorphism is one of the core concepts in OOP languages, it describes the concept that different
# classes can be used with same interface. Each of these classes can provide its own implementation of the interface.

# For this example we are going to create two distinct classes to use with two distinct objects, each of these
# distinct classes need to have an interface in common so that they can be used polymorphically, meaning two methods
# that are distinct but have the same name.
# ~ For the purpose of this example ~ I will be doing inheritance in the same class
class Fish:
    # Two attributes of Fish that will be inherited by the derived classes Shark and Clownfish, who will
    # add their own values according to what kind of fish they are, this demonstrates further the need for
    # polymorphic classes and methods in a class, it allows information to be displayed without know what kind of class
    # you are getting the information from.
    __type_of_fish = None
    __swim_speed = None

    def __init__(self):
        pass


class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.type_of_fish = "Elasmobranch"  # Adding custom value to the 'type_of_fish' variable
        self.swim_speed = 25  # Adding custom value to the 'swim_speed' variable

    def swin(self):  # Method of the Shark class but is also in the Clownfish class
        print("The shark can swim at a speed " + self.swim_speed.__str__() + "mph")

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards at " + round(self.swim_speed / 3, 2).__str__() + "mph")

    def skeleton(self):
        print("The shark's skeleton is made of cartilage. Also known as a " + self.type_of_fish)

    # This is just like __str__, it overrides the default print value of this class if it were to be printed out.
    def __repr__(self):
        return "\nAn instance of the shark class has been created"

class Clownfish(Fish):
    def __init__(self):
        super().__init__()
        self.type_of_fish = "Amphiprioninae"
        self.swim_speed = 20

    def swin(self):
        print("The clownfish is swimming at a impressive " + self.swim_speed.__str__() + "mph")

    def swim_backwards(self):
        print("The clownfish can swim backwards at just " + (self.swim_speed / 2).__str__() + "mph")

    def skeleton(self):
        print("The clownfish's skeleton is made of bone. Also known as a " + self.type_of_fish)

    def __repr__(self):
        return "\nAn instance of the Clownfish class has been created"


# Shark and Clownfish have three methods with the same name in common. However, each of the functionality
# of these methods differ for each class. but can all be called from one for loop, making it efficient and
# easily accessible to programs.

# Polymorphic_fish

sammy = Shark()
# sammy.skeleton()

casey = Clownfish()
# casey.skeleton()

# Two classes that can be iterated and provide outputs for each method call through a
# polymorphic variable such as fish are known as polymorphic methods
for fish in (sammy, casey):  # Creates a union of classes Clownfish and Shark
    print(fish)  # Access the __str__/ __repr__ methods inside a class to see what it is
    fish.swin()  # using fish as alias for both classes it will loop through each class looking for the method swim
    fish.swim_backwards()
    fish.skeleton()
