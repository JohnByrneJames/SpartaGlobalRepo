# We are doing a presentation on the OOP concept of Encapsulation
# This is where code examples of encapsulations will be made

# The concept of Encapsulation is to keep together the implementation (code) and the data it manipulates (variables).
# Having proper encapsulation ensures that the code and data both are safe from misuse by outside entity.
#
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age

    def display(self):
        print(self.name)
        print(self.__age)

    def change_age(self, new_age):
        self.__age = new_age


person = Person('John', 40)
#accessing using class method
person.display()
#accessing directly from outside
print('Trying to access variables from outside the class ')

person.display()
person.change_age(20)  # Change age via a method inside the class
person.display()
person.age = 19  # Cannot access private variable
person.display()

