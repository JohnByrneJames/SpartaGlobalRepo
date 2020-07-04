# What is an API
# Application programming interface
# Used to connect to other programs, data, interfaces and functions from third parties
# To use an API - python has a module called requests to interact with WEB-APIs

# How to get a python package in pyCharm
# We do the below code in the python to install the requests package
# >>> pip install requests

import requests

# check HTTP/HTTPS 200 [Success] - 400 [Bad Request] - 404 [Page not found]
# response_poke = requests.get("https://www.pokemon.com/us/")

# This can also be done with a . notation and 'status_code' as it returns just the code
# print(response_poke.status_code)  # Returns <Response [200]> [Success], Successfully made a request
# print(response_poke.headers)  # Prints out the headers of the response request
# print(response_poke.content)

# print(type(response_poke.headers))
# print(type(response_poke.content))

# Types of Requests
# GET: retrieve information (like search results). This is the most common type of request. Using it, we can get the
# data we are interested in from those that the API is ready to share.
# POST: adds new data to the server. Using this type of request, you can, for example, add a new item to your inventory.
# PUT: changes existing information. For example, using this type of request, it would be possible to change the color
# or value of an existing product.
# DELETE: deletes existing information

# Iteration 1
# receive a response and check if 200 - print success
# elif page not found
# else Sorry not page found

# Iteration 2
# create a function called check_response_code() including all the above
# returns the message with status code

# Iteration 3
# Use OOP and 4 Pillars (Encapsulation, Abstraction, Inheritance and Polymorphism)

# ~ Done in request_response.py ~
import requests
from request_response import RequestResponse

print("\n")

url = "https://national-weather-service.p.rapidapi.com/products/locations"

headers = {
    "x-rapidapi-host": "national-weather-service.p.rapidapi.com",
    "x-rapidapi-key": "927bcbee56msh9b0b9704a9d6484p1eaeb4jsn11c9ee903dcd",
}

response = requests.request("GET", url, headers=headers)

response_req = RequestResponse(response)
print(response_req.check_response_code())

data = response.json()



# print(data)
# print(data["503"]["name"])

# for name, id in data.items():
#     print(name, id)

# for key, value in employee_records.items():
#     if value == int:  # If the value is a integer
#         print(key, ":", int(value))
#         continue
#     if value == bool:  # If the value is a boolean
#         print(key, ":", bool(value))
#         continue
#     print(key, ":", value)
#
