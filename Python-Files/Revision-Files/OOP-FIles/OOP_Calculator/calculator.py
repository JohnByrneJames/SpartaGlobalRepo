from arithmetic import Arithmetic
# OOP Calculator

# Calculator using static methods to allow the user to perform calculations
class Calculator(Arithmetic):

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


