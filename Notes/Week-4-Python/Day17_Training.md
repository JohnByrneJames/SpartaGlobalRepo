###### Sparta Global Training Day 17
###### Going over Python concepts again to really get them, also we are covering the TDD (test driven development).

___

> 9:00 AM Stand-up [Morning]

I had a good day overall yesterday but I feel like I did not use the weekend to my advantage and left a shed load of
work for me to complete now in the week along with whatever work I am assigned. It is very unlike me but I feel like it is
just an improvement point and something that I can learn from in the future.

**Review of Individual Presentation**

Yesterday we did our individual presentation, it was 5 minutes that we were given to present our knowledge on OOP or object oriented
programming understanding in Python. We were also to give a coded example in PyCharm that was in the student_data format using the same
format throughout the examples, this was to make sure each example specifically made that OOP concept shine. There was also a need for a 
Elevator Pitch and then at the end a DOD which presented our confirmation that we did what was asked.

**3 Positive Points**
* The OOP concepts were well described in my opinion, they covered almost every point of the concepts including some
rather advanced concepts that others did not get covered by others such as the ABC (abstraction base class) module for abstraction and the Getter and
Setter in encapsulation.
* The presentation was quite visual and it laid out the points that were necessary in a visually stimulating slide show.
* The presentation was actually quite descriptive in the way it was conveyed which rather surprised myself too, as I have
noticed I am a little mono-tone past presentations. So I think that was a good improvement. 

**3 Constructive Points**
* The presentation needed a little more enthusiasm and energy that I did not have as I was a little nervous
as I am not used to presenting at all. This is a good opportunity to learn.
* I think my elevator pitch was a little sloppy as I did not prepare properly before hand due to myself rushing - this
was purely due to myself and lack of organisation.
* The presentation did not remain within the given time-box of 5 minutes, this is because I did not get to rehearse as I was
in such a rush to get the powerpoint ready and everything. I will become more prepared for these things in the future.

Thanks for the opportunity to learn more about myself and how I can improve, I would appreciate your own feedback on myself.

**Kind Regards, <br>
John Byrne**

___

> 10:00 AM Starting JSON [Mid-Morning]

##JSON

**JSON** - Javascript Object Notation

Syntax - JSON is syntax for exchanging data and is very similar to dictionaries in Python <br>
It is commonly used to send data between browser and server.

JSON is also used to parse the data from existing files or web browser.

The data can only be text - hence JSON is text written in JSON format. JSON will consider both numbers and strings
as a string-formatted variable.

**Data Types**

* A string
```json
{ "name":"John" } 
```

* A number
```json
{ "age":30 } 
```

* an object (JSON object)
```json
{
"employee":{ "name":"John", "age":30, "city":"New York" }
} 
```

* an array
```json
{
"employees":[ "John", "Anna", "Peter" ]
} 
```

* a boolean
```json
{ "sale":true } 
```

* null
```json
{ "surname":null } 
```

Where does this syntax derived from.
* In JSON data is in "**name**": "**value**" pairs: {Dictionary}

Below we are decoding and encoding a dictionary into a JSON file, this dictionary was first encoded into a
file using the `dump()` function and `load()` function for decoding the data out of the file and reading it
back into a python readable dictionary.

```python
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
for key, value in car.items():
     if value == int:  # If the value is a integer
         print(key, ":", int(value))
         continue
     if value == bool:  # If the value is a boolean
         print(key, ":", bool(value))
         continue
     print(key, ":", value)

# We have decoded our file new_json_file.json that we created earlier
# We have used dumps(), dump() and load() methods
# The load method has returned the JSON file as a dictionary
```

We did a programming exercise using a JSON file that was full of conversion rates using a euro as a base currency,
with this we were to take the data and make it usable and more efficient in ways we have learnt. 
Find my exercise here [**Conversion.Py**](../../Python-Files/JSON/json_exchange_rates.py)

It is easy to think of it like this:
* **Encoding** is usually witting to a file.
* **Decoding** is usually reading from a file.


* **web-browser - app - cloud**
* **on premise data**

>API call to HTTP request (web-browser) <br>
>>Response from HTTP (Json file)

This is an interaction that takes places when we make a request using Pythons Requests Module. The browser
is able to understand a request and translates a request based on the information given and returns it in a response
to the one making the request.
**Errors** will arise if you try to request data that is either private or inaccessible to us using error codes like
404, 503, 502.

For an example we were doing [**postcodes**](../../Python-Files/JSON/json_parsing_with_api.py) we could enter our own postcode
and it would load all the data from london postcodes courtesy of [**postcode.io**](https://api.postcodes.io/)

```python
import requests
import json
post_codes_req = requests.get("https://api.postcodes.io/postcodes/ig89pt")

print(post_codes_req.status_code)

if post_codes_req.status_code == 200:
    print("Success")
elif post_codes_req.status_code == 404:
    print("Page unavailable")

print(post_codes_req.headers)
print(type(post_codes_req.headers))
print(post_codes_req.content)
print(type(post_codes_req.content))
print(post_codes_req.json())
type_json = post_codes_req.json()
print(type(type_json))
```

**Types of Requests in API:**
* HTTP
* Header ➜ {Key : Value} Pairs
* Body ➜ [Date available: **TEXT**, **JSON**, **XML**]
* Content 
* Status

**Data type in URL:**
* XML
* HTML
* JavaScript
* JSON

We send a HTTP request and we get a response according to the response code, as mentioned above. When we
send a request we send it on a URL basis and that is recognised by the server and returns the data that you are expecting.

**RESTful API**

**CRUD** stands for "**Create**, **Read**, **Update**, and **Delete**" which are four basic database operations. Many HTTP services
also model CRUD operations through REST or REST-like APIs. In this tutorial, you will build a very simple web API to manage a list of products... 
The products API will expose the following methods.

___
**Homework** 
* Friday one-to-ones are on Trello board
    * Elevator Pitch
    * coding test/ exercise (python only...)

