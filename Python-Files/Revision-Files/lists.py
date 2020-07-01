# Data Collection

# In Java they use Arrays / However in Python lists are same as arrays
# Both serve same purpose of storing data
# Good at managing data - Access data in order - it gives us option to add, remove data (mutable)

# Syntax of list [ a list ] square brackets (tuples) and {dictionary - key:value}
# Tuples are immutable and lists are mutable. (the data cannot be changed)

cities = ["Tokyo", "Paris", "Prague", "Luxembourg"]

# Display is another word for print
# Print cities

# Print out the cities list
print(cities)

# Print out the type of content in this case <case 'list'>
print(type(cities))

# Access Luxembourg in the cities list E.G. the 3rd index of the list
print(cities[3])

# We can replace the index at 3 (Luxembourg) as lists are mutable
# In this case we have replaced it with Amsterdam
cities[3] = "Amsterdam"
print(cities[3])

# Add another city to the list with the .append function
cities.append("Vilnius")
print(cities)

# Here we are removing a city from the list with the remove function
# Can also remove at the index cities.remove(cities[1])
# cities.remove("Paris")
# print(cities)

# The pop function will remove the last index in a list
# cities.pop()

# This will insert a entry into the list at any specified index
# This moves back the item that was previously at that position.
cities.insert(0, "London")
print(cities)

print()  # Space in the terminal print

# Lists can store different types of data such as integers and strings
mix_type_string = [1, 2, 3, "One", "two", "Three"]
print(mix_type_string)

# Lists can hold multiple lists, in this case two
mix_type_string = [[1, 2, 3], ["One", "two", "Three"]]
print(mix_type_string)