# OOP - 4 pillar of object oriented programming
# 1 - Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# 2 - Polymorphism
# This allows us to define methods in a child class with the same name as defined in their parent class.
# Using the same name helps your program look more intuitive and easier.
# A child class inherits all methods from the parent class, however in some situations
# the method inherited from the parent doesnt fit the child class.

# 3 - Encapsulation
# The idea of wrapping data and methods that work on data within one unit. It puts restrictions on
# on accessing variables and methods directly and can prevent the accidental modification of data.
# To prevent accidental change, an object’s variable can only be changed by an object’s method.
# Those type of variables are known as private variable.

# 4 - Abstraction
# Abstraction means hiding the complexity and only showing the essential features of the object.
# This is achieved using abstract classes and interfaces. An abstract class is a class that generally
# provides incomplete functionality and contains one or more abstract methods. Abstract methods are the methods
# that generally don’t have any implementation, it is left to the sub classes to provide implementation for the
# abstract methods.

# This is how you define the class dog, it has a predefined value in the breed which is "shorkie"
# It can be initiated by requires to know the name and color of that dog
class Dog:
    breed = "Shorkie"

    def __init__(self, name, color):
        self.name = name
        self.color = color

    @staticmethod
    def bark():
        return "Woof Woof!"

    @staticmethod
    def sleep():  # This is a static method meaning it can be called even without an instance of the class
        return "ZZZzzzzzz"

    # This self variable refers to the instance that is being used, it is used to retrieve its stored variables.
    # In this case the fact that jack_the_dog is a called "Jack" and is "golden".
    def play(self):
        return "The " + self.color + " pooch bounces around after the ball"

    def run(self):
        return self.breed + "'s are commonly known to be very! fast runners"

    def eat(self):
        return self.name + " is a big fan of dog mooch!! nom nom nom... \n" + self.sleep()


# Here an instance of the class Dog has been made and stored inside the variable jack_the_dog
# You can access methods inside an instance by leading with a . to bring up the usable methods.
jack_the_dog = Dog("Jack", "golden")
print(jack_the_dog.name + " The " + jack_the_dog.color + " " + jack_the_dog.breed)

print(jack_the_dog.eat())
print()

print(jack_the_dog.bark())

# ~ Exercise ~
# Create sleep, breath, run, eat methods that can be called
