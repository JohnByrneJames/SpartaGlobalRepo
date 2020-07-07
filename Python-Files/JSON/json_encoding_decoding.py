# python JSON module Javascript object notation
# Why - we create an object

import json

# ENCODING from dictionary and writing to JSON file
car_data = {"name": "tesla", "engine": "electric", "top_speed": 155}  # Dictionary
print(car_data)

# printing the dictionary

print(type(car_data))
# Checking the type of dictionary

# print(car_data)

car_data_json_string = json.dumps(car_data)  # a dump()
# Json.dump() changes python dict to str

print(type(car_data_json_string))  # JSON format changed the type to an string

# Creating a JSON file with writing permission
# enter the name of the file, permission type ("w") = write
with open("new_json_file.json", "w") as jsonfile:  # Encoding

    json.dump(car_data, jsonfile)  # json.dump takes 2 arguments
    # The first argument is the dictionary created (car_data)
    # The second argument is the file type which is json_file on this occasion

# Encoding and creating and writing into the created json_file

with open("new_json_file.json") as jsonfile:  # Decoding
    # Reading from the file we just created
    car = json.load(jsonfile)  # storing data from file to car variable
    print(type(car))  # checking the type of the car object
    print(car['name'])  # display value of key 'name'
    print(car['engine'])  # display value of second key 'engine'
    print(car['top_speed'])

# Relatively efficient way to print out dictionary keys and values.
# for key, value in car.items():
#     if value == int:  # If the value is a integer
#         print(key, ":", int(value))
#         continue
#     if value == bool:  # If the value is a boolean
#         print(key, ":", bool(value))
#         continue
#     print(key, ":", value)

# We have decoded our file new_json_file.json that we created earlier
# We have used dumps(), dump() and load() methods
# The load method has returned the JSON file as a dictionary
