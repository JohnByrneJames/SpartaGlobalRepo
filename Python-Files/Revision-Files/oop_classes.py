# Classes
# Naming convention for creating a class is to capitalise the first letter
# Syntax - class 'class_name'

# Everything in a class is an object
class PyCalculator:
    def __init__(self, number1, number2):  # Self keyword points to the class itself
        self.num1 = number1
        self.num2 = number2

    def addition(self):
        return self.num1 + self.num2

    def subtract(self):
        return round(self.num1 - self.num2, 2)

    def multiplication(self):
        return self.num1 * self.num2

    def modulate(self):
        return self.num1 % self.num2

    def division(self):
        return round(self.num1 / self.num2, 2)


# ~ Exercise ~
# Create a basic calculator inside a class
# Should have methods to add, subtract, divide, modulate and multiply

num1 = input("Please enter two numbers. \n Number 1 :  ")
num2 = input(" Number 2 :  ")

# This function checks if the input from the user is a integer or a float and returns the correct type
# So string to float if its a decimal or string to integer if its a whole number
def integer_float_converter(number):
    try:
        val = int(number)
        return val
    except ValueError:
        try:
            val = float(number)
            return val
        except ValueError:
            print("No.. input is not a number. It's a string")
            exit()


calculator = PyCalculator(integer_float_converter(num1), integer_float_converter(num2))

print()  # Space in terminal

print(calculator.num1.__str__() + " + " + calculator.num2.__str__() + " = " + calculator.addition().__str__())
print(calculator.num1.__str__() + " - " + calculator.num2.__str__() + " = " + calculator.subtract().__str__())
print(calculator.num1.__str__() + " x " + calculator.num2.__str__() + " = " + calculator.multiplication().__str__())
print(calculator.num1.__str__() + " % " + calculator.num2.__str__() + " = " + calculator.modulate().__str__())
print(calculator.num1.__str__() + " ÷ " + calculator.num2.__str__() + " = " + calculator.division().__str__())