# Using the built-in python libraries such as the Math library

# These are library imports, they can be imported and give us access to all of their predfined functions
from random import random
import math

# This is a functionality available in math known as random
# it will return a random number every time the program is run
print(random())

# This is a float, we will be applying functions within the math library to see what is possible
float_num = 24.5  # Float
print(math.ceil(float_num))  # Round up the float from 24.5 to 25
print(math.floor(float_num))  # Round down the float from 24.5 to 24

# pi figure = 3.14 it is a constant in maths and is the ratio of a circles circumference
print(math.pi)

print()  # Space in terminal


# Create a method that would take 2 arguments
# Calculate cm into inches
# 7 inches into cm - make sure to follow good naming conventions, such as cm_to_inches describes what the function does
def cm_to_inches(cm):
    return round(cm / 2.54, 2)


users_input = float(input("Please enter your centimeter calculation :  "))

print(str(users_input) + " cm converts into " + str(cm_to_inches(users_input)) + " inches")
