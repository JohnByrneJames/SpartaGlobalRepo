class Vehicle:  # Vehicle class - in this example it is the super class E.G. the parent class
    # These are the attributes of the vehicle class, they are predefined within the class, so they can be privatised if
    # needed.
    color = None
    wheels = [2, 4, 8]
    horse_power = None
    doors = [0, 2, 4]
    license_plate = None
    miles_per_gallon = None

    # This is the Vehicle classes initialisation method, here some attributes are populated with values, and it also
    # creates a blueprint of sort for the derived classes that may need to access these attributes/ methods.
    def __init__(self, color, wheels, horse_power, license_plate, doors=4):
        self.color = color
        self.wheels = wheels
        self.horse_power = horse_power
        self.license_plate = license_plate
        self.doors = doors

    # Ask the user for two inputs and store them into two separate variables to calculate the miles per gallon
    # for a vehicle. This is also accessible through any defined class that has declared super().__init__ to inherit
    # these attributes and methods.
    def miles_per_gallon_method(self):
        miles_driven = float(input("How many miles have you driven since your last fill up?  "))
        gallons_fueled = float(input("How many gallons have you filled up?  "))
        self.miles_per_gallon = round(miles_driven / gallons_fueled, 2)
        print("Your vehicle uses " + self.miles_per_gallon.__str__() + "mpg ")

    def print_details(self):
        pass

