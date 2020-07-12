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

> From a functions perspective :
>
> A parameter is the variable listed inside its parentheses in the function definition.
>
> An argument is the value that is sent to the function when it is called

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
