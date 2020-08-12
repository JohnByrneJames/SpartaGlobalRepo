from vehicle import Vehicle
from car import Car
from sports_car import SportsCar

# Inheritance class

# Before starting this I am going to layout the idea behind the inheritance example, you can also find
# a more in depth view of it on the README_OLD.md file located at the main page of this directory.
# This file will demonstrate how inheritance allows child classes to adopt the methods and functionality available
# in its parent class and adding any additional functionality on top. This helps reduce the amount of duplicated code
# as it is bad practice to keep repeating yourself.

# An instance of class is defined here and the required arguments have been passed into the class constructor,
# this is then taken and used to create a instance of a class, in this case a Car called Bess which is the colour red,
# and has a horse power of 300+

# Bess = Car("Red", 4, 300, "YB07 FGP", "Mini Cooper", "2019", True, 4)
# Bess.print_details()
# Bess.change_number_plate()
# Bess.print_details()
McLaren = SportsCar("Orange", 4, 755, "XR J0HN", "McLaren 765LT ", "2020", False, 2, False, 205)
McLaren.race()
McLaren.change_number_plate()  # A method defined originally in the Car Class
McLaren.miles_per_gallon_method()  # A method defined originally in the Vehicle class
