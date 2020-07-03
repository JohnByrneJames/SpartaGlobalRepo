class Arithmetic:

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

