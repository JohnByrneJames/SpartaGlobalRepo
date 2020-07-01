# strings - casting - slicing - concatenation

# Single quote will give error as it has a single quote inside the string too
# ~ ERROR ~ #
# print ('Ugne's class is eng67')

# To work around single quote you use a / before the ' apostrophe to allow it inside the string
print('Ugne\'s class is eng67')

# Double quotes are usually the safer bet as they hand the single quotes inside without any attention
print("Ugne's class is eng67")

greeting_today = "Hello Ma' friend"
print(greeting_today)
# H E L L O   M A '    F  R  I  E  N  D
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

# -16                                 -1

# This prints out len
print(len(greeting_today))

# indexing

# welcome_user = input("Please enter your name  ")
# print(" Dear " + welcome_user + " Welcome on board!")

# String SLICING
# ~ Remember ~ Indexing starts at 0

name = "Hello world"

#print(name[10])  # print index 10 - E.g. d
#print(name[6:11])  # print index 6 - 10 E.g. World
#print(name[0:4])  # print index 1 - 3 E.g. Hell
#print(name[-5:-1])  # prints index -1 to -5 E.g. worl

remove_white_space = "remove the space the end of a string with spaces"
# This string has len = 49 characters
print(len(remove_white_space))

# This will remove the spaces from the string at start and end len = 47 characters
print(len(remove_white_space.strip()))

# Boolean value with DATA types

use_text = "Here's SOME text WITH lots of text"

# Count() counts the substring within the string
# This will count all places where 'text' is present = 2
print(use_text.count("text"))

print(use_text.count("t"))

print()  # This is just for spaces in the terminal

# Changes a strings output into all lower case
print(use_text.lower())

# Changes a strings output into all upper case
print(use_text.upper())

# Changes the first letter of each word into a capital
print(use_text.title())

# Changes the first letter of the string capitalized and the rest lower case
print(use_text.capitalize())

# replacing text in the string with what is specified replace("look for", "replace with")
print(use_text.replace("t", "!"))

# Comparison if string starts with h, case sensitive so 'h' is False and 'H' is True
print(use_text.startswith("h"))
print(use_text.startswith("H"))
