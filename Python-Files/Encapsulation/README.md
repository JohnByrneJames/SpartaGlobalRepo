# Encapsulation

## **Contents**

- [x] What [:file_folder:](#What?)

- [x] Why [:file_folder:](#Why?)

- [x] How [:file_folder:](#How?)

- [x] Getter and Setter [:file_folder:](#getter-and-setter)

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

```python
# Outside scope of Person Class
person = Person()
print(person.name)
print(person.print_name())

# This will return an attribute error
print(person.__last_name)

# This will return an attribute error
print(person.__private_method())
```

Trying to print out either of these private methods or attributes will throw an attribute error at the user, this is because they no longer exist
in the class to anyone accessing from outside the scope. It is actually there but has been renamed therefore the user will be told it cannot be
accessed outside the class.

There is in fact one way to access these private methods outside the class, it is done using a technique known as name-mangling,
private attributes can also be accessed this way but have a proper technique of which is generally used which I will come onto in a little bit.

```python
# Outside scope of Person Class
person = Person()

# object._Class__attribute/method name (name Mangling)
print(person._Person__private_method())  
print(person._Person__last_name)
```

The method can now be accessed by entering what the interpreter has renamed it, this is a done by accessing the method
via its class, this makes the interpreter assume you are accessing the method from within the classes scope and will not
return an error. the same can be done with the attributes.

**To conclude**
* Single **_** create protected members, they should not be accessed directly. But nothing stops you from doing that (except convention).
* Double **_ _** create private members, harder to access than the private ones but still accessible non-the-less.
* Both are accessible, but private by convention.

# Getter and Setter

Private variables are intended to be changed using the getter and setter methods. These provide indirect access to them.
This allows the change to take place within the class method and can help keep data integrity as it will only
change the instances attributes. You can also apply additional checks inside the getter and setter methods to check
for conditions.

```python

class Person:
    # Inside scope of Person Class
    def __init__(self):  
        self.name = "John"  # public attribute
        self.__last_name = "Byrne"  # private attribute
        self._age = 22  # protected attribute

    def print_name(self):
        return self.name + " " + self.__last_name

    def public_method(self):  # public method
        return "This method is public, welcome!!"

    def __private_method(self):  # private method
        return "This method is private! I love cake! How are you seeing this?!"

    # Setter method
    def setlastname(self, last_name):
        print("set last_name() called")
        self.__last_name = last_name

    # Getter method
    def getlastname(self):
        print("get last_name() called")
        return self.__last_name

    last_name = property(getlastname, setlastname)


person = Person()
person.last_name = "Orpin"  # Set the last_name
print(person.last_name)  # Get the last_name, return the last name 
```

As you can see when you make a change to a private variable through this technique it will give you a message,
and it will also give a message when you try to retrieve it. The property() function allows you to assign an alias
in place of the get and set methods to access their contents, the interpreter will take care of running it when it detects
a change or retrieval of that private attribute. It can also be done a slightly different way using a decorator called @property

Find the implementation of this in the python class here [**encapsulation.py**](encapsulation.py)