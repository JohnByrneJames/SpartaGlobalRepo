import requests
import json
post_codes_req = requests.get("https://api.postcodes.io/postcodes/se167tq")

print(post_codes_req.status_code)

# Why should we use built-in packages
# you do not need to do a comparison operator as the requests.get will already check the code for us before
# # we are do the comparison in the if statement below with == 200. ~ first iteration
# if post_codes_req.status_code == 200:
#     print("Success")
# elif post_codes_req.status_code == 400:
#     print("Bad Request")
# elif post_codes_req.status_code == 404:
#     print("Page unavailable")
# elif post_codes_req.status_code == 500:
#     print("Server Error")

# This can be done without the comparison operators ~ second iteration
# if post_codes_req.status_code:
#     print("Success")
# elif post_codes_req.status_code:
#     print("Bad Request")

# Below is the same functionality but with OOP - class and a method ~ third iteration
class LiveWebStatusCode:

    @staticmethod
    def check_status_code(response):
        if response is not None:
            if response == 200:
                print("Success")
            elif post_codes_req.status_code == 400:
                print("Bad Request")
            elif post_codes_req.status_code == 404:
                print("Page unavailable")
            elif post_codes_req.status_code == 500:
                print("Server Error")
        else:
            print("Error checking the code")
            return


# Check the status code of this request and return correct response
LiveWebStatusCode.check_status_code(post_codes_req.status_code)

# print(post_codes_req.headers)
# print(type(post_codes_req.headers))
# print(post_codes_req.content)
# print(type(post_codes_req.content))
# print(post_codes_req.json())
type_json = post_codes_req.json()
# print(type(type_json))

print(type(type_json))

class JSONReader:

    def get_all_values(self, nested_dictionary):  # This is a method
        for key, value in nested_dictionary.items():  # iterate through the key, value pairs in this dictionary
            if type(value) is dict:  # if the value of a key is a dictionary, then you have found a nested dictionary
                self.get_all_values(value)   # recall this method passing in that dictionary to iterate through it
            else:
                print(key, ":", value)  # if the value of the dictionary is not a dict carry on looping through


json_reader = JSONReader()
json_reader.get_all_values(type_json)  # Returns all the values inside a dictionary including any nested dictionaries

