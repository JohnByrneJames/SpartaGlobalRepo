import datetime
import time
import os

class FavoriteFood:

    def get_users_favourite_food(self):
        # Get user input
        try:
            users_input = input("What is your favorite food :")
            # raise exception error
            if len(users_input) is 0:
                raise ValueError
        except ValueError:
            # catch exception
            # give error message
            print("Input field has been left blank...")
            FavoriteFood.__add_error("Input field empty")
        else:  # No issues with input
            self.__latest_favourite(users_input)

    @staticmethod
    def __latest_favourite(food):
        print("Adding your favorite food to the list... :) 2 seconds")
        with open("favourite_food.txt", "w+") as file:  # "w+" allows me to read and write
            file.write("{0}, favourite food added at {1}".format(food.__str__(), FavoriteFood.__get_current_datetime()))
            print("\nWriting...")
            time.sleep(0.3)
            print("Writing completed successfully...")
            file.seek(0)  # Reposition pointer at the first character in the file, which is 0
            FavoriteFood.__update_favourites_history(file.read())

    @staticmethod
    def __update_favourites_history(food):
        print("Now copying favourite_food to permanent history...")
        time.sleep(1)
        if os.path.exists("favourite_food_history.txt") is False:  # If file doesnt already exist add header
            with open("favourite_food_history.txt", "a+") as file:  # append this onto a permanent history file
                file.write("Permanent History of favourite Food\n")  # If file doesn't exist add header
                file.write("\n\n" + food)
        else:
            with open("favourite_food_history.txt", "a") as file:  # append this onto a permanent history file
                file.write("\n\n" + food)

    @staticmethod
    def __add_error(error):
        error = "You have encountered an error... | " + error
        print("You have encountered an error...")
        time.sleep(1)
        print("Adding it to the file history for future improvements...")
        FavoriteFood.__update_favourites_history(error)

    @staticmethod
    def __get_current_datetime():
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M")

