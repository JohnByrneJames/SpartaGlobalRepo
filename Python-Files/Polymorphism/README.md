# Polymorphism

## **Contents**

- [x] What [:file_folder:](#What?)

- [x] Why [:file_folder:](#Why?)

- [x] How [:file_folder:](#How?)


# What?

Polymorphism is one of the core concepts of OOP, it describes the concept that different classes can be used with the same
interface, e.g. the same method name or iterating value. It is essentially the ability for different types to respond to the same
function call. 

One of the most simple occurrences of Polymorphism in Python is demonstrated below:

**Example 1**
```python
num1 = 1
num2 = 2
print(num1 + num2)
```
**Example 2**
```python
str1 = "Python"
str2 = "Programming"
print(str1 + " " + str2)
```

We know that the '+' operator is used extensively in Python programs. But, it does not have a single usage.
* For the integer types, '+' operator is used to perform arithmetic addition operation.
* For the string data types, '+' operator is used to perform concatenation. As a result, the above program outputs Python programming. 

Here, we can see that a single operator + has been used to carry out different operations for distinct data types. This is one of the most simple occurrences of polymorphism in Python.

We can use the concept of polymorphism while creating class methods as Python allows different classes to have methods with
the same name. We can then later generalise calling these methods by disregarding the object we are working with. Lets look at
an example.

 # Why?
 
Polymorphism is useful as it makes programming more intuitive and therefore easier, it is easier to understand how a
class it doing its functionality but not really how. It is also a fancy word that means the same method is defined in different objects of
different types (different classes). 

Polymorphism is a very important concept in programming. It refers to the use of a single type entity (method, operator or object) to 
represent different types in different scenarios. 

 # How?
 
For this example we are going to create two distinct classes to use with two distinct objects, each of these
distinct classes need to have an interface in common so that they can be used polymorphically, meaning two methods
that are distinct but have the same name.

**Fish Class**
```python
class Fish:
    __type_of_fish = None
    __swim_speed = None

    def __init__(self):
        pass
```

**Shark Class**
```python
class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.type_of_fish = "Elasmobranch"
        self.swim_speed = 25  

    def swin(self):
        print("The shark can swim at a speed " + self.swim_speed.__str__() + "mph")

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards at " + round(self.swim_speed / 3, 2).__str__() + "mph")

    def skeleton(self):
        print("The shark's skeleton is made of cartilage. Also known as a " + self.type_of_fish)

    def __repr__(self):
        return "\nAn instance of the shark class has been created"
```

**Clownfish Class**
```python
class Clownfish(Fish):
    def __init__(self):
        super().__init__()
        self.type_of_fish = "Amphiprioninae"
        self.swim_speed = 20

    def swin(self):
        print("The clownfish is swimming at a impressive " + self.swim_speed.__str__() + "mph")

    def swim_backwards(self):
        print("The clownfish can swim backwards at just " + (self.swim_speed / 2).__str__() + "mph")

    def skeleton(self):
        print("The clownfish's skeleton is made of bone. Also known as a " + self.type_of_fish)

    def __repr__(self):
        return "\nAn instance of the Clownfish class has been created"


sammy = Shark()
casey = Clownfish()
for fish in (sammy, casey):  # Creates a union of classes Clownfish and Shark
    print(fish)  # Access the __str__/ __repr__ methods inside a class to see what it is
    fish.swin()  # using fish as alias for both classes it will loop through each class looking for the method swim
    fish.swim_backwards()
    fish.skeleton()
```

Here there are three classes, that have been defined with the same interface. However, each of the fuctionality
of these methods differ for each class. These can actually be iterated through as they are polymorphic methods, making it efficient
and easily accessible to programs regardless of data that is going to be printed.

We have also used a built-in polymorphic method available in Python known as the `__repr__` which is a formal version of
`__str__ `and made it prompt the user whenever a instance of a class has been instantiated.

The print statement at the end is looping through the arguments which are the instances of a class, since they have
polymorphic methods that are related in terms of interface name, they can be iterated through and produce their own
unique outputs. This has also been done with the 'print(fish)' which calls the `__repr__` we made earlier.

When you loop through two objects that share polymorphic interfaces it is said you have made a union between these two
objects **Shark** and **Clownfish**.

Find the implementation of this in the python class here: <br> 
[**Polymorphism.py**](Polymorphism.py) 
