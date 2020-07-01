# Sets are very similar to Lists
# Sets are unordered unlike Lists [Indexing]

# Syntax of Set {} curly brackets

# This is how you create a set
car_part = {"Wheels", "Windows", "Doors"}
print(car_part)

print(type(car_part))

# Adding an item to the Set
car_part.add("Seats")
print(car_part)

# Deleting an item in the Set
car_part.discard("Windows")
print(car_part)

print()  # Space in terminal

# Frozen Set
# Syntax is () and store them in a variable
# This is a immutable Set
counting = frozenset([1, 2, 3, 4])
print(counting)
print(type(counting))
