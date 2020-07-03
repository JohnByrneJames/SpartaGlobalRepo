# OOP Calculator

class Calculator:

    @staticmethod
    def addition(value1, value2):
        return value1 + value2

    @staticmethod
    def multiplication(value1, value2):
        return value1 * value2

    @staticmethod
    def subtraction(value1, value2):
        return value1 - value2

    @staticmethod
    def division(value1, value2):
        return value1 / value2

    @staticmethod
    def modulate(value1, value2):
        return value1 % value2

    @staticmethod
    def get_numbers():
        num1 = int(input("Enter first number:  "))
        num2 = int(input("Enter second number: "))
        return num1, num2

    @staticmethod
    def get_operator():
        operator = input('Please enter an operator (+, -, *, %, /): ')
        return operator

    @classmethod
    def calculate(cls):
        num1, num2 = cls.get_numbers()
        operator = cls.get_operator()
        if operator == '+':
            print(cls.addition(num1, num2))
        elif operator == '-':
            print(cls.subtraction(num1, num2))
        elif operator == '*':
            print(cls.multiplication(num1, num2))
        elif operator == '%':
            print(cls.modulate(num1, num2))
        elif operator == '/':
            print(cls.division(num1, num2))
        return


calc = Calculator()

print("Welcome to the calculator")
while True:
    print("/n")
    calc.calculate()

    decision = input("Want to do another calculation (Y/ N)  ")
    if decision.lower() == "y":
        continue
    elif decision.lower() == "n":
        break





