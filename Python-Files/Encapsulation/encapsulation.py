# Encapsulation

# Encapsulation is the packing of data and functions operating on that data into a single component
# and restricting the access to some of the object's components. It essentially means the internal representation of
# an object is generally hidden from view outside of the objects definition.

# A good example is a class, it encapsulates all the data that its member methods and attributes have.

# Some would say that Encapsulation is very similar to Abstraction, however there is one major difference :
# Encapsulation = Information hiding
# Abstraction = Implementation hiding

# Protected member is declared with the use of a _ by convention. This tells others "don't touch this, unless you are a
# subclass of this class".
# Private members can be defined in python, you add a __ in front of the member to hide them from when accessing
# them from out of the class.

class Person:
    # Inside scope of Person Class
    def __init__(self):  # The __init__ method is a constructor and runs as soon as the class is instantiated.
        self.name = "John"  # public attribute
        self.__last_name = "Byrne"  # private attribute
        self._age = 22  # protected attribute

    def print_name(self):
        return self.name + " " + self.__last_name

    def public_method(self):  # public method
        return "This method is public, welcome!!"

    def __private_method(self):  # private method
        return "This method is private! I love cake! How are you seeing this?!"

    # Example of getter and setter method - not usually used in Python
    # But better practice for formally setting attributes values
    # Setter method
    def setlastname(self, last_name):
        print("set last_name() called")
        self.__last_name = last_name

    # Getter method
    def getlastname(self):
        print("get last_name() called")
        return self.__last_name

    last_name = property(getlastname, setlastname)


# Outside scope of Person Class
person = Person()
print(person.name)
print(person.print_name())

# Attribute Error: 'Person' object (class) has no attribute '__last_name'
# This is because the attribute last name does not exist to anyone trying to access the class from outside.
print(person.__last_name)
# The same can be applied to methods inside a class, this can be done with the same __.

print()  # Add Space in the terminal

# Outside scope of Person Class
# print(person.public_method())

# Attribute Error: 'Person' object has no attribute '__private_method'
# Again this method is private therefore cannot be accessed outside the person class.
# >>> print(person.__private_method())

# This is called a mangled method, by changing the name you an actually access this private method.
# Showing that the private function doesn't actually provide much protection. Accessing a private member like
# this should be refrained as it is bad practice.
# print(person._Person__private_method())  # object._Class__private_method (name Mangling)

# Essentially when a variable has been made private python will perform name mangling, effectively changing the name
# of the variable to '_object._class__variable'.

# This below is possible as the property() function has been used and allows appropriate assignment
# and retrieval of the last_name attribute form outside the class scope.
# person.last_name = "Orpin"  # Set the last_name even though it is private
# print(person.last_name)  # Get the last_name, return the last name (despite it being private)
