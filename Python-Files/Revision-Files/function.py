import math


# Function
# It is a block of code that can be executed at any time throughout the program multiple times
# D R Y - DO-NOT REPEAT YOURSELF
# The whole idea of functions is to minimise the code and make it more reusable.

# Syntax -def `name_of_function`(any_parameter(s)):

# To define a function you use the keyword def and you can include parameters inside its brackets
# these are variables that are sent into the function and can be used in the operation
# We are creating a Greeting function here to greet the user
def greeting():
    return "Hello World"  # Return a value to the call
    pass  # This is used to exit out of functions that do not do anything (yet) ... during development


# The function will not run unless it has been called and if it requires parameters/arguments
# then it needs the those to run without an error
print(greeting())  # function call - gets the return value if any...


# Here the dog function receives a parameter/arguments of type string from the call function, it is the breed of a dog
# this is placed in the breed placeholder, this is then utilised in the output to the user.
def dog(breed, age):
    human_age = round((16 * math.log(age)) + 31, 2)

    return "\nWow! you're dog is so cute! I am a big fan of " + breed + "'s. \n It has an age of " + str(human_age) \
           + " in human years "


print(dog("Greyhound", 6))


# Functions should be simple and do one job, instead of trying to achieve multiple functionalist's. Usually the simpler
# the better as users can easily identify what the function does from its name.

# ~ Exercise ~
# Create a function with two args to return a addition of 2 values
def addition(value1, value2):
    return value1 + value2


# Create a function with two args to return a multiplication of 2 values
def multiplication(value1, value2):
    return value1 * value2


# Create a function with two args to return a subtraction of 2 values
def subtraction(value1, value2):
    return value1 - value2


# Create a function with two args to return a division of 2 values
def division(value1, value2):
    return value1 / value2


# Create a function with two args to return a remainder of 2 values
def remainder(value1, value2):
    return value1 % value2


# NEEDS TO BE FIXED

number_1 = int(input("Enter a number : "))
number_2 = int(input("Enter another number : "))

print(number_1.__str__() + " + " + number_2.__str__() + " = " + addition(number_1, number_2).__str__())
print(number_1.__str__() + " x " + number_2.__str__() + " = " + multiplication(number_1, number_2).__str__())
print(number_1.__str__() + " - " + number_2.__str__() + " = " + subtraction(number_1, number_2).__str__())
print(number_1.__str__() + " / " + number_2.__str__() + " = " + division(number_1, number_2).__str__())
print(number_1.__str__() + " % " + number_2.__str__() + " = " + remainder(number_1, number_2).__str__())

print()  # Add space in terminal
# create a function with multiple args

def multi_args(*multiargs):  # Unpacking allows any amount of varaiables to be passed into a function
    print(type(multiargs))

    for args in multiargs:
        print(args)
    return args


print(mult_args(1, 2, 3, 5, 6, 6, 7, 1))
