# Variables File

# Need good naming conventions camelCase or snake_case

pay = 10  # Integer or int
hours = 1.5  # Float or float
name = "Spartan"  # String or str

number = input("What is your spartan number?  ")  # Input from the user will be stored in this variable.

# Added Variables into print
print(name + "-" + number + " makes $" + pay.__str__() + " every " + hours.__str__() + " Hours...\n")

# built in method called type()
print(type(pay))
print(type(hours))
print(type(name))

# Adds space in terminal print
print()

# 10 x 1.5
print(pay * hours)

# Spartan + 10 - convert the int to a string via the str() or __str__
print(name + " " + str(pay))

# Overwrite a variable - the pay of the spartan
x = "20"  # Pay is now 20

# ~#~ Exercise : User Details ~#~
# Create a variable called first_name and last_name
# Create a variable called full_name and display the full_name
# Create a variable called age
# Create a variable called address
# Prompt the user to get all the above information

first_name = input("What is your first name?  ")
last_name = input("\nWhat is your last name?  ")

full_name = first_name + " " + last_name

age = input("Great! Nice to meet you " + full_name + ". How old are you?  ")
address = input("\nAnd what is your address?  ")

print("Alright, to confirm " + full_name + ". You are " + age + " years old and live at " + address + "...")

# print("Alright, to confirm {0}. You are {1} years old and live at {2}...".format(full_name, age, address))