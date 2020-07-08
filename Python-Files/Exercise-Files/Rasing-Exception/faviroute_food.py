import time

class FavoriteFood:
    # create predetermined error message
    # create predetermined success message

    def get_users_favourite_food(self):
        # Get user input
        try:
            users_input = input("What is your favorite food :")
            # raise exception error
            if len(users_input) == 0:
                raise ValueError
            elif type(users_input) != str:
                raise TypeError
        except TypeError:
            print("#{0} Received - Please only enter alphanumeric characters".format(str(type(users_input))))
        except ValueError as e:
            print(e)

        # catch exception

        # give error message

        # Write users input to a file

        # Read from file and write to another file



# 1.
# Accept from the user some text.Ensure user enters something else raise an
# exception.
# After that write that text to a file and then read
# from this file to write to another file simultaneously
# 2.
# Reading an image to writing to another file simultaneously

