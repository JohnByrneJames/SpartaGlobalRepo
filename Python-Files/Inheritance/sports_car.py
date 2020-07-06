from car import Car

# This class is similar to the last class except it is inheriting from Car, which has inherited from vehicle - therefore
# it gets all the attributes and methods available from both classes. It adds two attributes for the SportsCar class
# which is a derived class of the car class.
class SportsCar(Car):  # is sub class of Car
    is_a_classic = None
    top_speed = None

    def __init__(self, color, wheels, horse_power, license_plate, car_manufacturer, year_car_was_made,
                 is_manual, doors, is_a_classic, top_speed):
        super().__init__(color, wheels, horse_power, license_plate, car_manufacturer, year_car_was_made,
                         is_manual, doors)
        self.is_a_classic = is_a_classic
        self.top_speed = top_speed

    # Using scientific equations to figure out the time it would take for a sports car to finish a circuit, these are
    # made up of three pre-determined values meaning miles. Using Distance / speed you can work out the time it takes
    # to finish a race.
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