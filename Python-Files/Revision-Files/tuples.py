# A tuple is like a list but the main difference is immutable
# You are not able to do anything to this during run-time apart from view the data
# Store data that would not need changing i.e. date-of-birth, passport number, ethnicity

# Syntax of Tuple: we use ( ) to declare a Tuple

person = ("name", "date of birth", "passport number")
print(person)

print(type(person))  # The tuple is a tuple here

# ~ Exercise ~
# Convert the tuple into a string
# Add your name into the string at 0 index
# Display the string

# To edit a tuple you need to convert it into a list
# Once it is a list make the changes
tuple_to_list = list(person)
tuple_to_list[0] = "John"

print()
print(type(tuple_to_list))  # The tuple is a list here
print()

# Once the changes have been done I converted it back into a tuple
person = tuple(tuple_to_list)

print(type(person))   # The tuple is a tuple again here

print(person)