# Inheritance

## **Contents**

- [x] What [:file_folder:](#What?)

- [x] Why [:file_folder:](#Why?)

- [x] How [:file_folder:](#How?)


# What?

Inheritance allows us to define a class that inherits all methods and properties from another class:
* **Parent class** is the class being inherited from, also called the base class.
* **Child class** is the class that inherits from another class, also called the derived class.

To inherit: <br>
* **class**(parent_class)

**Examples** 

The program that I have written to demonstrate the concept of inheritance, uses a vehicle to
describe how it could be used in a real world example. This is seen as if there is a base class called 'vehicle', then that
class will define all the necessary attributes and methods that vehicles share, then a child class that is specifically focused on
'cars' will be able to inherit that information and add car-exclusive attributes and methods. This is the concept of inheritance, it allows us to reuse code that has been written
and add on top of it where needed. Again to further this example, we could add a 'sports_car' class which is a further
break down of the car and has its own unique attributes and methods. Along with a couple fancy methods and
functionality the example is quite intuitive.

**Inheritance Layout**
* **Vehicle** Parent Class
    * **Attributes**
        * color
        * Wheels
        * horse_power
        * doors
        * license_plate
        * miles_per_gallon
    * **Methods**
        * miles_per_gallon_method
        * print_details

* **Car** Child Class to **Vehicle**
    * **Attributes**
        * car_manufacturer
        * year_car_was_made
        * is_manual
    * **Methods**
        * change_number_plate
        * print_details  `overrides` **Vehicle** `method`

* **SportsCar** Child Class to **Vehicle** and **Car**
    * **Attributes**
        * is_a_classic
        * top_speed
    * **Methods**
        * race
        
Remember that all these classes are inheriting all of the attributes and methods from their parent classes.

 # Why?
 
When you inherit from another class it is a very good way of keeping your program DRY (don't repeat yourself), this allows
us to inherit methods and attributes from another class that may be needed but along with new attributes and methods
that can be defined in the derived classes initialisation function. This is **re-usability** of code. 
 
 # How?
 
To use inheritance you need to use be able to understand how the chain of inheritance works, if you want to copy of the attributes and methods
you need to use a special keyword in your init method, called 'super()' this inherits all the attributes and methods from its
parents.

```python
class Vehicle:
    color = None
    wheels = [2, 4, 8]
    horse_power = None
    doors = [0, 2, 4]
    license_plate = None
    miles_per_gallon = None

    def __init__(self, color, wheels, horse_power, license_plate, doors=4):
        self.color = color
        self.wheels = wheels
        self.horse_power = horse_power
        self.license_plate = license_plate
        self.doors = doors

    def miles_per_gallon_method(self):
        miles_driven = float(input("How many miles have you driven since your last fill up?  "))
        gallons_fueled = float(input("How many gallons have you filled up?  "))
        self.miles_per_gallon = round(miles_driven / gallons_fueled, 2)
        print("Your vehicle uses " + str(self.miles_per_gallon) + "mpg ")

    def print_details(self):
        pass

# Instantiating an instance of this class
a_vehicle = Vehicle("Red", 4, 900, "E7RY72", 2)

a_vehicle.miles_per_gallon_method()
# >>> How many miles have you driven since your last fill up?  100
# >>> How many gallons have you filled up?  20
# >>> Your vehicle uses 5 mpg
```

Here we have defined the class Vehicle and assigned it some specific arguments in its initialisation, this means that when an instance of this class is created,
it will throw an error if it doesn't receive its required arguments. From this example you are
expected provide a color, wheels, horse_power, license_plate and doors. Then two methods have been defined
with some custom functionality, any child class that derives from this class will have access to these methods.

```python
import time
from vehicle import Vehicle  # Allows vehicle to be derived from 

class Car(Vehicle):
    car_manufacturer = None
    year_car_was_made = None
    is_manual = None

    def __init__(self, color, wheels, horse_power, license_plate, car_manufacturer, doors, year_car_was_made,
                 is_manual):
        super().__init__(color, wheels, horse_power, license_plate, doors=4)
        self.car_manufacturer = car_manufacturer
        self.year_car_was_made = year_car_was_made
        self.is_manual = is_manual

    def change_number_plate(self):
        print("\nCurrently your number plate is " + self.license_plate)
        while True:
            new_license_plate = input("\nPlease enter your new number plate :   ")
            new_license_plate = new_license_plate.replace(" ", "") 
            if len(new_license_plate) > 7 or len(new_license_plate) < 6:
                print("\nNumber plates can only be 6 - 7 characters.")
            else:
                print("Changing your number plate... to " + new_license_plate)
                print("\n50%")
                time.sleep(.900)
                print("\n100% - Complete!")
                time.sleep(.900)  # Perform a small pause between printing to imitate loading, from time package
                self.license_plate = new_license_plate
                break

    def print_details(self):
        print("Your details are as follows:  \n" + "Car_manufacturer :" + self.car_manufacturer + "\n" +
              "year_car_was_made :" + self.year_car_was_made + "\n" + "is_manual: " + self.is_manual.__str__() + "\n" +
              "license_plate: " + self.license_plate.__str__() + "\n")

Bess = Car("Red", 4, 300, "YB07 FGP", "Mini Cooper", "2019", True, 4)
Bess.print_details()
Bess.change_number_plate()
Bess.print_details()
Bess.miles_per_gallons_method()  # A method inherited from the Vehicle Class
```

Here we are inheriting the Vehicle class, this is shown as the `__init__` method in the top has a `super()` function which
tells us that it is inheriting the attributes and methods from its parent class. if you are planning on adding extra
features to the derived class, such as more attributes you need to declare in the super class which attributes you are inheriting,
typically all the previously defined ones and then in the `__init__` you can add extra attributes. These are then assigned when
you instantiate this new class.

This classes instances are also able to access the methods of its parent class, in this case Vehicle and its `miles_per_gallon_method`
which is not visibly in this class. 

```python
from car import Car

class SportsCar(Car):  # is sub class of Car
    is_a_classic = None
    top_speed = None

    def __init__(self, color, wheels, horse_power, license_plate, car_manufacturer, year_car_was_made,
                 is_manual, doors, is_a_classic, top_speed):
        super().__init__(color, wheels, horse_power, license_plate, car_manufacturer, year_car_was_made,
                         is_manual, doors)
        self.is_a_classic = is_a_classic
        self.top_speed = top_speed

    def race(self):
        track_size = input("\nWhat size track do you want to race around? [L] [M] [S]  ")
        if track_size.lower() == 's':  # Lower case the track_size as then it will always match the small cases
            track_size = 1
            track_time = round(1609 / self.top_speed, 2)
        elif track_size.lower() == 'm':
            track_size = 2
            track_time = round(3218 / self.top_speed, 2)
        elif track_size.lower() == 'l':
            track_size = 4
            track_time = round(6437 / self.top_speed, 2)
        else:
            print("Invalid input")
            return

        print("It took the " + self.car_manufacturer + " " + str(track_time) + " seconds to go " + str(track_size) +
              " miles")

McLaren = SportsCar("Orange", 4, 755, "XR J0HN", "McLaren 765LT ", "2020", False, 2, False, 205)
McLaren.race()
McLaren.change_number_plate()  # A method defined originally in the Car Class
McLaren.miles_per_gallon_method()  # A method defined originally in the Vehicle class
```

This is the final class which inherits from the Car class which in turn has already inherited from the Vehicle class, this means that
it gets access to all the methods and attributes from them both. You can see how easy this makes development when you are creating similar objects that may derive
from a single object but differ with slight unique differences.

**Importantly** you should always remember if your class is in a different file then you will need to import it
from that class using the correct path and Class name.

Find the implementation of this in the python class here: <br> 
[**Inheritance.py**](inheritance.py) `This is the file that has the queries to the classes` <br>

[**Vehicle**](vehicle.py) `This is the base class for car and SportsCar` <br>
[**Car**](car.py) `This is the child class of Vehicle` <br>
[**SportsCar**](sports_car.py) `This is the child class of Car and Vehicle`
