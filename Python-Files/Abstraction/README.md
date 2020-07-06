# Abstraction

**Contents**

- [ ] What [:file_folder:](#What?)

- [ ] Why [:file_folder:](#Why?)

- [ ] How [:file_folder:](#How?)
    - [ ] Important Points [:file_folder:](#important-points)

### What?

Abstraction is another concept of OOP wherein the user is kept unaware of the basic implementation of a functions
property. The user is only able to view basic functionality whereas the internal details are hidden from view. The aim is
to allow the user to know what they are doing but not how the work is being done.

**Examples** 
* :blue_car: When a person gets into a car, they expect the car to do what it is intended to. If they press the gas they expect
the car to go forward, if they press the horn they expect the car to make a "beep" noise. They are not expected to know, understand or even
care how the car moves forward or how it produces the noise for the horn they just want to use the car as a whole, without knowing
its inner workings or each individual component that make up that car. :red_car:
* :atm: When a person goes to an ATM to withdraw money they just want to access their funds and carry out whatever business they
 need to do, whether it be withdrawing or depositing. They don't care how th machine keeps track of their balance or how it retrieves the money
 they just want to be free to use the ATM as a whole. meaning they just want to enter an amount and receive that amount. It may
 be a complex process behind the scenes but it is not important to the user so its an abstract of that functionality.:bank: 
 
 ### Why?
 
 Abstraction is used to handle the complexity of an object, this is usually accomplished through something known as
 hierarchical abstraction which will be demonstrated through the python file that is in this repository. As previously mentioned as well
 the process of abstraction allows the developer to hide all irrelevant data/ processes that take place in an application in order to reduce
 complexity and increase efficiency.
 
 ### How?
 
 In python abstraction is achieved by using abstract classes and methods in our programs. A class containing one or more
 abstract methods is called a abstract class. Abstract methods do not contain any implementation. Instead, all the implementation can be defined in methods
 of sub-classes that inherit the abstract class. An abstract class is created by importing a class named 'ABC' from the 'abc' module and
 inheriting the 'ABC' class. Below is the syntax for creating the abstract class.
 
```python
from abc import ABC

class AbsClass(ABC):
```
 
 The 'ABC' is imported to and inherited by the class 'AbsClass'. The class 'AbsClass' becomes an abstract class when we define the
 first abstract method using the '@abstractmethod' annotation. As we already discussed, abstract classes should not contain any implementation,
 therefore the method should contain simple a 'pass' statement.
 
 ```python
from abc import ABC

class AbsClass(ABC):

    @abstractmethod
    def task(self):
        pass
``` 

Here task is the abstract method of the abstract class 'AbsClass'. The implementation of the abstract class can be defined
in the sub-classes that inherit from class 'AbsClass'. In the below example, 'TestClass' and 'ExampleClass' are the two
sub-classes that inherit the abstract class 'AbsClass'.

```python
from abc import ABC

class AbsClass(ABC):

    @abstractmethod
    def task(self):
        pass


class TestClass(AbsClass):
    def task(self):
        print("We are inside the TestClass task method")


class ExampleClass(AbsClass):
    def task(self):
        print("We are inside the ExampleClass task method")
```

If the implementation of the abstract method is not defined in the derives classes, then the python interpreter will throw an
error. This is because the abstract method will not be defined as a working method, therefore it must have some kind of base
implementation / functionality.

### Important Points

There are also some important points to take into consideration when creating abstract classes/ methods in Python.
1. An abstract class can have both a normal method and an abstract method
2. An abstract class cannot be instantiated, i.e., we cannot create objects for the abstract class
3. 'ABC' is the module to be imported when we define an abstract class in Python programs. 'abc' stands for 'abstract base class'.

An abstract class having a normal method and a abstract method.

In the below example, 'print' is a normal method defined inside the abstract class 'AbsClass' in this example, it is able to perform
a print value function for instantiated classes of the non abstract classes 'ExampleClass' amd 'TestClass'. 

```python
from abc import ABC

class AbsClass(ABC):
    # normal method
    def print(self, x):
        print("Passed value : ", x)

    @abstractmethod
    def task(self):
        pass


class TestClass(AbsClass):
    def task(self):
        print("We are inside the TestClass task method")


class ExampleClass(AbsClass):
    def task(self):
        print("We are inside the ExampleClass task method")


# object of TestClass class
testclass = TestClass()
testclass.task()
testclass.print(100)

# object of ExampleClass class
exampleclass = ExampleClass()
exampleclass.task()
exampleclass.print(200)
```

Here the normal method is called from the 'main()' method using an object created for the child classes 'ExampleClass' 
and 'TestClass'.

Find the implementation of this in the python class here [**abstraction.py**](abstraction.py)