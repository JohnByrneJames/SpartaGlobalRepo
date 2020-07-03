from xmlrpc.client import boolean

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
        return "A Baby!"

    def move(self):
        pass

