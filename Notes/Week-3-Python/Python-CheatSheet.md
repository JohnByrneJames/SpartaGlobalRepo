# Python Cheat Sheet
### As a learning reinforcement I will be going through the W3Schools Python Course too
### This is the course at [**W3Schools**](https://www.w3schools.com/python/python_variables.asp), I will be recording my progress with examples where needed for future reference.

<div align="center" style="font-weight: bolder">:rainbow: By John Byrne :rainbow:</div> 

___

# Legend :key:
* This is a block of code, it is intractable and incorporates highlighting for easier reading.
```python
print("Hello world")  
```

* A Progress test or exercise will be recorded with a link to the exercise taken (click the :clipboard: icon) and record of score. <br>
  
    * Python Variable Test :arrow_forward: [:clipboard:](Day12_Training.md)  :star: **97%** :star:

* The contents of this Cheat-sheet is labelled at the top, to jump to a section simply click the :file_folder: next to the section name.
    - [ ] Python Variables [:file_folder:](#contents-page_facing_up) `Pending`
        - [ ] Further Variables [:file_folder:](#contents-page_facing_up)
        
    - [x] Python Variables [:file_folder:](#contents-page_facing_up) `Complete` 
        - [x] Further Variables [:file_folder:](#contents-page_facing_up)
           
# Contents :page_facing_up:
- [ ] Comments [:file_folder:](#comments)
- [ ] Variables [:file_folder:](#variables)
- [ ] Data Types [:file_folder:](#data_types)
- [ ] Numbers [:file_folder:](#numbers)
- [ ] Casting [:file_folder:](#castings)
- [ ] Strings [:file_folder:](#strings)
- [ ] Booleans [:file_folder:](#booleans)
- [ ] Operators [:file_folder:](#operators)
- [ ] Lists [:file_folder:](#lists)
- [ ] Tuples [:file_folder:](#tuples)
- [ ] Sets [:file_folder:](#sets)
- [ ] Dictionaries 
- [ ] If...Else
- [ ] While Loops
- [ ] For Loops
- [ ] Functions [:file_folder:](#functions)
- [ ] Lambda
- [ ] Arrays
- [ ] Classes/ Objects
- [ ] Inheritance
- [ ] Iterators
- [ ] Scope
- [ ] Modules
- [ ] Dates
- [ ] Math
- [ ] JSON
- [ ] RegEx
- [ ] PIP
- [ ] Try...Except
- [ ] User Input
- [ ] String formatting

# Comments

# Functions

A function is a block of code which only runs when it is called, it is also referred to as a method
when it is encapsulated inside a class. You can pass data, known as parameters, into a function. A function
can take that data and return a result made of data. It is good practice to make functions perform one
and only one function to keep simplicity of a program.

## Creating a function

In python a function is created by using the `def` keyword followed by the name of the function and parentheses which
can have arguments if there are any.

```python
def my_function():
    print("Hello from a function")
```

## Calling a function

A function is called when its name is mentioned in code along with parentheses and any other required arguments,
this will then make the interpreter step into that function when it is running through code
at run-time.

```python
def my_function():
    print("Hello from a function")

my_function() 
```

## Arguments

Information can be passed into functions as arguments, these arguments are specified after the function name, 
inside parentheses. You can add as many arguments as you want, just separate them by a comma. A argument is called an argument
because it is what will be used inside that function, this is an ideal way of using a piece of code to perform a
specific function as the arguments could contain relative information. When the function is called, we pass along a first name,
which is used inside the function to print the full name.

```python
def my_function(fname):
    print("Welcome " + fname)

my_function("John")
my_function("Cliff")
my_function("Jack")
```

In the documentation for python the arguments of a function are usually shortened to `args` this
is a common expression used by python programmers to define functions that take multiple parameters, in some
cases arguments that are passed regardless of how many (dynamic) arguments.

### Parameters and Arguments

The terms parameter and argument can be used for the same thing: information that are passed into a function.

**From a functions perspective** :

* A parameter is the variable listed inside its parentheses in the function definition.
* An argument is the value that is sent to the function when it is called

By default, a function must be called with the correct number of arguments or it will return an error saying how few or too many arguments
are missing. This means that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
If you call a function with an incorrect number of arguments you will get a `TypeError`, saying that it is
missing 1 required positional argument : "parameter_name"

```python
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("John", "Byrnes") 
``` 

## Arbitrary Arguments (*args)

If you do not know how many arguments will be passed into your function, add a * before the parameter name in the function. The *
in many languages stands get or take all of the incoming data. This way the function will receive a `tuple` of arguments, and it can access the items accordingly.

_It is common practice in python that Arbitrary arguments are shortened to *args in most documentation_

```python
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "John", "Tobias", "Linus") 
```

> In this example the function has been called with 4 arguments, this is acceptable as the `my_function` parameter
> is an arbitrary argument and takes any number of arguments signified by the * before the name of the argument. This is
> stored in a `tuple` which can be accessed through indexing. However if there were short of 3 arguments this code would throw an error
> as the tuple produced would only have 2 pieces of data.

## Keyword Arguments

Arguments are also able to be sent to a function with the `key` = `value` syntax. This way the order of the arguments does not matter,
this can be useful if you are not aware of when the argument is required in a function but know the names of each parameter that
has been specified.

```python
def my_function(child3, child2, child1):
  print("The youngest child is " + child2)

my_function(child1 = "Emil", child2 = "John", child3 = "Linus") 
```

_The phrase keyword argument is often shortened to kwargs in Python documentation_

## Arbitrary Keyword arguments (**kwargs)

If you do not know how many keyword arguments will be passed into a function, add two ** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly. This is a combination of the last two
topics: Keyword arguments and arbitrary arguments, this allows you to store and access the data in a `key` = `value` format.

```python
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname ="Tobias", lname = "Byrne")
```

_Arbitrary keyword arguments are often shortened to **kwargs in Python documentation_

## Default Parameter Value

It is also possible to assign a default value to a parameter in a function, this means that this does not need to be
specified when a call is made to that function. This can be useful when a value is not specified 100% of the time or there is a
existing or permanent value for an argument. If we call the function without argument, the default value if specified will be used.

```python
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()  # Norway
my_function("Brazil") 
```

## Passing a [List](#Lists) as an argument

You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type
inside the function. The flexibility of to transfer data so easily makes functions an amazing way to create efficient and powerful programs. 

```python
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
```

_If you send a list it will be a list when it reaches the function and can be iterated through as shown_

## Return Values

When a function is called usually it is expected to do something with the data it has received, this data can then be returned to the
caller using the `return` keyword followed by whatever value you would like to return. This is extremely handy as it allows for
componentisation of functions, E.G. to create functions that are designed to accomplish a specific task and return an output.

```python
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9)) 
```

## The Pass Statement

function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the
`pass` statement to avoid getting an error. The pass statement essentially tells the interpreter to pass this function and carry on
running through the code. This is most commonly used to help map out the design of a function or class in larger programs and
prevent the console from throwing an error whilst testing is taking place.

```python
def my_function():
    pass
```

## Recursion

Python also accepts function recursion, which means a defined function can call itself. Recursion is a common mathematical and programming concept.
It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
A good example of where this is used is a function that is designed to loop through a dictionary and continue recursion until it has
looped through all if any of its nested dictionary.

```python
def get_all_values(nested_dict):

    for key, value in nested_dictionary.items():
        if type(value) is dict:
            get_all_values(value)
        else:
            print(key, ":", value)

nested_dictionary = {"dict1": {"a": 1},"dict2": {"b": 2}}
```

_The need to loop and reveal data through nested dictionaries is quite common when using API as it a common way the data is recieved_

The developer should be very careful with recursion as it can quite easy to slip into writing a function which never terminates, or one that uses
excess amounts of memory or processor power. However, when written correctly recursion can be very efficient and mathematically-elegant approach to programming.
If a process requires a similar process for each iteration then recursion is an ideal solution.

```python
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

```

_This code creates 6 instances of the method calling itself until the `k` value = 0_

_When the `k` value = 0 it will start returning which will go through all the classes until has reached the initial function call_

This code can be quite hard to understand just by looking at it, so I have created a table that contains the workings of it.
It goes through the initial creation of the recursion loop that was created until the condition was met
from that point it unravels the recursion loop and returns the results accordingly.

| Return #      | Result value | K value | Equation    | Return value |
|---------------|--------------|---------|-------------|--------------|
| Initial Call  | -            | 6       | -           | -            |
| Instance 2    | -            | 5       | -           | -            |
| Instance 3    | -            | 4       | -           | -            |
| Instance 4    | -            | 3       | -           | -            |
| Instance 5    | -            | 2       | -           | -            |
| Instance 6    | -            | 1       | -           | -            |
| Condition Met | -            | 0       | -           | 0            |
| Return 1      | 0            | 1       | 0 + 1 = 1   | 1            |
| Return 2      | 1            | 2       | 1 + 2 = 3   | 3            |
| Return 3      | 3            | 3       | 3 + 3 = 6   | 6            |
| Return 4      | 6            | 4       | 6 + 4 = 10  | 10           |
| Return 5      | 10           | 5       | 10 + 5 = 15 | 15           |
| Return 6      | 15           | 6       | 15 + 6 = 21 | 21           |

