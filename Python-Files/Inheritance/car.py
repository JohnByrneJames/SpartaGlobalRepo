import time
from vehicle import Vehicle

# This is the derived Car class which is a generic class for all cars and if used in a large scale program would be the
# parent class of different types of cars to inherit from as it contains methods and attributes that are useful when
# identifying a car specifically.
class Car(Vehicle):  # subclass of Vehicle
    car_manufacturer = None
    year_car_was_made = None
    is_manual = None

    # Here the Vehicles __init__ function has been overridden to include all its previous parameters, these allow
    # the car to be initialised with all the attributes that were defined in the Vehicle class, it also defines a
    # couple unique attributes that are exclusively for the cars class.
    def __init__(self, color, wheels, horse_power, license_plate, car_manufacturer, year_car_was_made,
                 is_manual, doors):
        super().__init__(color, wheels, horse_power, license_plate, doors=4)
        self.car_manufacturer = car_manufacturer
        self.year_car_was_made = year_car_was_made
        self.is_manual = is_manual

    def change_number_plate(self):
        print("\nCurrently your number plate is " + self.license_plate)
        while True:
            # Ask the user what they want to change their license_plate to, then uses a if statement to check whether
            # the new license_plate is valid E.G. 6 - 7 characters
            new_license_plate = input("\nPlease enter your new number plate :   ")
            new_license_plate = new_license_plate.replace(" ", "")  # Remove all the blank spaces so it can be counted
            if len(new_license_plate) > 7 or len(new_license_plate) < 6:  # Should be between 7 and 6 characters
                print("\nNumber plates can only be 6 - 7 characters.")
            else:
                print("Changing your number plate... to " + new_license_plate)
                print("\n50%")
                time.sleep(.900)
                print("\n100% - Complete!")
                time.sleep(.900)  # Perform a small pause between printing to imitate loading, from time package
                self.license_plate = new_license_plate
                break

    # This prints out all the relevant information for the car
    def print_details(self):
        print("Your details are as follows:  \n" + "Car_manufacturer :" + self.car_manufacturer + "\n" +
              "year_car_was_made :" + self.year_car_was_made + "\n" + "is_manual: " + self.is_manual.__str__() + "\n" +
              "license_plate: " + self.license_plate.__str__() + "\n")