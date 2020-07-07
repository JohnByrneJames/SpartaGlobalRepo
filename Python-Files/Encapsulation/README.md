# Encapsulation

## **Contents**

- [x] What [:file_folder:](#What?)

- [x] Why [:file_folder:](#Why?)

- [x] How [:file_folder:](#How?)

- [x] Important Points [:file_folder:](#important-points)

# What?

Encapsulation is the packing of data and functions operating on that data into a single component and restricting the access
to some of the the object's components. It essentially means the internal representation of an object us generally hidden from
view outside of the objects definition. Some would say that encapsulation is very similar to abstraction, however this one key difference
between the two: <br>
* **Encapsulation** = Information hiding
* **Implementation** = Implementation hiding

Two types of Altercations: <br>
* **Protected** = **_** `_protected_method`
* **Private** = **_ _** `__private_method`

**Examples** 

Although a lot of developers would argue that encapsulation does not exist in Python :snake: as the keyword to make
methods and attributes private is not documented as a proper implementation, unlike some other object oriented languages, but
encapsulation can still be achieved. Instead it relies on the convention: **"** A class variable that should not be directly accessed
should be prefixed with an underscore **_**.

**Getter and Setter**

There is a proper convention in most OOP languages that design a integral way to retrieve and manipulate private variables. To
access and change private variables accessor (getter) methods and mutator (setter methods) should be used which are part of
the class. This can also be made better by using the 'property' function which allows you to set two classes which are a getter and
setter classes.

 # Why?
 
If everything inside a class is public then you will put your class and its members at risk to accidental manipulation,
by setting a private/ protected variable you are adding that extra layer of protection that will prevent users from accessing it from
outside the class. To a degree at least as it can still be accessed you a technique known as 'Name-Mangling'. This essentially means that there is
no explicit access modifiers and everything written within the class is public by default.
 
 # How?
 
As mentioned private keyword, does not explicitly exist in python and it has part convention and part trust
through implementation. 

```python

class Person:
    # Inside scope of Person Class
    def __init__(self):  
        self.name = "John"  
        self.__last_name = "Byrne"  
        self._age = 22  

    def print_name(self):
        return self.name + " " + self.__last_name    

    def public_method(self):  
        return "This method is public, welcome!!"

    def __private_method(self):  
        return "This method is private! I love cake! How are you seeing this?!"
    # End of scope in Person Class
```

Here the Person class has been created, it has three variables:
* **name** = public variable
* **_age** = protected variable
* **__last_name** = private variable 

and three methods:
* **print_name** = public method
* **public_method** = public method
* **__private_method** = private method

The reason for this simple naming convention is to produce an example that is not too complex and demonstrates the power of
encapsulation in its whole form. 

So here if we were to try create an instance of the Person class, we could actually access the _age variable as it is only protected
by convention, but the __firstname is private and has been name mangled by the python interpreter. However this can still be accessed
through specifying the mangled name, this will be demonstrated below.




Find the implementation of this in the python class here [**encapsulation.py**](encapsulation.py)