import requests
import json
post_codes_req = requests.get("https://api.postcodes.io/postcodes/ig89pt")

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
if post_codes_req.status_code:
    print("Success")
elif post_codes_req.status_code:
    print("Bad Request")

# Below is the same functionality but with OOP - class and a method ~ third iteration
class CheckStatusCode:
    response = None

    def response_code(self, response):
        if response is not None:
            self.response = response.status_code
        else:
            print("Error checking the code")
            return


print(post_codes_req.headers)
print(post_codes_req.content)
print(post_codes_req.json())
type_json = post_codes_req.json()
print(type(type_json))
