# Loops
# For Loops : Used to iterate through lists, Strings, Dictionaries, Tuples, and other collections.

list_date = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # List
print(list_date)

# for loops iterates through the values inside the list and prints them out
# The x variable takes the value of each value every iteration of the loop
"""
for number in list_date:
    print(number)
"""

print()   # Space in the terminal

# combining if statement and for loop
# Indentation is important in this, break needs to be within the block of the for loop
# block will actually break stop the loop when the condition is met
# Continue will actually start the next iteration of the loop whenever it is called, rather than on reaching the end of
# the loop.
for number in list_date:
    if number > 5:
        break
    elif number == 2 or number == 3:
        print(str(number) + " is the Best!")
        continue
    print(number)

# You can also loop through a string, in terms of its indexes
# Here the string is picked apart and printed in one line "J O H N   B Y R N E"
name = "John Byrne"
in_one_line = ""

for index in name:
    in_one_line += " " + index
    if name[-1] == index:
        print(in_one_line)

print()  # Space in terminal

# This can also print out a dictionary using a loop
# You can either print out the keys or values
student_record = {
    "name": "John Byrne",
    "stream": "DevOps",
    "topics_completed": 5,
    "completed_lessons_name": ["Strings", "Tuples", "Variables"]
}

for key in student_record:
    print(key)

print()  # Space in Terminal

# ~Exercise~
# Dictionary with employee records minimum 5 key value pairs
# Use loop to iterate through
# Display the values and keys of the dictionary

employee_records = {
    "name": "John Byrne",
    "martial_status": "Married",
    "Age": 22,
    "Favorite_food": "Salmon",
    "Position": "DevOp",
    "Happy": False
}

# print out key and value of dictionary and if the value is a int then convert it to a integer, this stops any errors
# Surprisingly if you dont do a convert it will just stop and not throw an error
for key, value in employee_records.items():
    if value == int:  # If the value is a integer
        print(key, ":", int(value))
        continue
    if value == bool:  # If the value is a boolean
        print(key, ":", bool(value))
        continue
    print(key, ":", value)
