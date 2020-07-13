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
- [ ] Variables 
- [ ] Data Types 
- [ ] Numbers 
- [ ] Casting 
- [ ] Strings 
- [ ] Booleans 
- [ ] Operators
- [ ] Lists 
- [ ] Tuples [:lock:](#tuples)
- [ ] Sets 
- [ ] Dictionaries 
- [ ] If...Else
- [ ] Loops [:dizzy:](#Loops)
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


<div align="center" style="font-weight: bolder">---------- End of **Comments** ----------</div> 

___

# Tuples

A tuple is one of many collection types available in python. However, it has its own advantages and disadvantage which make it
preferable in certain situations. A tuple is a collection which is **ordered** and **immutable**(unchangeable). In python tuples are written
with round brackets **()**.

```python
a_tuple = ("hello", "world", "from", "python")
print(a_tuple)
```

_This is how you create a tuple, however in this case some data has been stored on declaration_

## Access Tuple Items

You can access tuple items by referring to the index. This is a common practice in many languages, the index is referred to inside square brackets
**[the_index]**. _Remember indexes start at 0_.

```python
a_tuple = ("apple", "banana", "cherry")
print(a_tuple[1])  # banana
```

### Negative Indexing

Negative indexing means beginning from the end of a collection. In this case `-1` refers to the last item, `-2` refers to the second
last item and so on.. This can be especially useful when you are trying to iterate through an unknown amount of items in a tuple and want to stop
when it is iterating over the last item, E.G. index **[`-1`]**

```python
a_tuple = ("apple", "banana", "cherry")
print(a_tuple[-1])  # cherry
```

### Range of indexing

You can specify a range of indexes by specifying where to start and where to end the range. When specifying a range, the return value will be a
new tuple with the specified items. This quite similar to the `range()` keyword however it is used in a different context, which is indexing to a tuple and
retrieving certain items.

```python
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])  # ('cherry', 'orange', 'kiwi')
```

_The search will start at index 2 (included) and end at index 5 (not included), remember indexes start at 0_

### Range of negative indexing

Same as the range of index except we are working backwards from the end to the start using negative indexes.

```python
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])  #('orange', 'kiwi', 'melon')
```

_Similarly to the `range()` operator this will only return the start the end index, not including the last index E.G. `-1` in this example._

## Change Tuple Values

Once a tuple is created, you cannot change its values. Tuples are **immutable** so cannot be changed.
But there is a workaround, you can covert a `tuple` into a `list`, change the `list`, and covert the `list` back into a `tuple`.

It may seem a little extensive but a `tuple` is ideal for storing data that does not generally change, such as a number plate or
phone extension code.

```python
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)  # ("apple", "kiwi", "cherry") 
```

_Here the item at index `1` which was banana has been changed to the kiwi, then it is converted back into a tuple
and printed to show the changes have been made_

_Attempting to change a tuples value will throw: `TypeError: 'tuple' object does not support item assignment`_

## Loop Through a Tuple

You can loop through the `tuple` items by using a `for` loop. 

```python
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
```

Find more information about [for loops](#for-loops)

## Check if item Exists

To determine if a specified item is present in a tuple use the `in` keyword, this checks over the entire tuple to find a match
of whatever was specified.

```python
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") 
```

## Tuple Length

To determine how many items a tuple has, use the `len()` method.

```python
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))  # 3
```

_The `len()` method is useful in a lot of situations to get the size of something, this case
it sees that the tuple has 3 items so it will return 3 as the length._

## Add Items

Once a tuple is created, you cannot add item to it. Tuples are again **IMMUTABLE**.

Again this is an error and it cannot be done, to do this refer to the above example, which
converts the `tuple` into a `list` to make changes and then changes it back again.

## Create Tuple with One item

To create a tuple with only one item, you have to add a comma ater the item, otherwise Python will not recognise it as a
`tuple`. This is a common mistake as if you don't add the comma the Python interpreter may think of it as a single variable assignment
just within parentheses.

```python
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) 
```

_In this example, the second one is actually just a string inside parentheses to the interpreter._

##Remove Items

_You cannot remove items from a `tuple`._

Again, `tuples` are **immutable**, so you cannot remove items from it, but you can delete the tuple completely.

```python
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists 
```

_The `del` keyword actually deletes the entire tuple, so it is no longer in the memory and has been
garbage collected_

## Join Two Tuples

To join two or more tuples you can use the `+` operator.

```python
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) 
``` 

_A single tuple has been made, formed of both `tuple1` and `tuple2`_

## The Tuple() Constructor

It is also possible to use the `tuple()` constructor to make a tuple.

```python
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
```

## The Tuple Index() Method

* The `index()` method finds the first occurrence of the specified value.
* The `index()` method raises an exception if the value is not found.

```python
thistuple = (1, 3, 7, 8, 7, 5, 
            4, 6, 8, 5)

x = thistuple.index(8)

print(x) 
```

_The above example returns **`3`** as the number `8` is the fourth element in this tuple
therefore starting from 0 it is the 3rd index_

_One thing to remember about this is that it will only return the first occurrence of a value, 
this can be good when used in conjunction with a loop and exception to loop until an exception is raised._

## The Tuple Count() Method

* The `count()` method returns the number of times a specified value appears in a tuple.

```python
thistuple = (1, 3, 7, 8, 7, 5,
            4, 6, 8, 5)

x = thistuple.count(5)

print(x) 
```

_The above example returns `2` as the number `5` has appeared in the sequence two times._



# Loops

In Python there are two primitive loop commands:
* [`while`](#while-loops) loop
* [`for`](#for-loops) loop

Loops are traditionally used when you have a block of code which you want to
repeat a fixed number of times. The Python `for` statement iterates over the members of a
sequence in order, executing the block each time. On the other hand you have the `while` loop
which iterates an infinite amount of times until it is told to stop or a condition is no longer satisfied.

# While loops

The `while` can execute a set of statements as long as the condition is `True`. The condition can be set to something that is
always true to enable an infinite loop or a boolean which can be altered during the loop execution.

```python
i = 1
while i < 6:
    print(i)
    i+=1
```

_The above example uses the increment operator to increase the variable `i` each iteration_

_Ultimately `i` will increase beyond 6 consequently exiting the while loop as the condition relies of `i` being less than 6_

Sometimes the variable used to exit the `while` loop is known as a indexing variable as it documents to number of times
a loop has iterated through its contents.

## The Break Statement

The `break` statement allows us to stop the loop even if the `while` loops condition is `True`. By using the break statement any
kind of looping or control-flow function can be exited before its execution path as it tells the interpreter to step outside the encapsulated
statement.

```python
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 
```

_On first observation this loop looks like it will exit after 5 iterations, however the if statement
which will become true when the i variable is 3 will call the `break` statement which will exit the loop._

_Therefore this loop will only iterate over its contents 3 times_

## The Continue Statement

The `continue` statement is similar to the `break` statement in the fact that it manipulates the flow of a loop,
however the `continue` statement stops the current iteration, and continues the the next one. This can be quite useful
if you want a loop to skip a particular loop of its contents.

```python
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
```

_Here we expect 6 iterations of the `while` loop, however it has been specified that `if` the `i` variable
is equal to 3, the `continue` statement will be called which will move onto the next iteration of the loop E.G 4_

_As a result the print function is never called on the 3rd iteration, therefore it will only print out 1, 2, 4, 5 and 6_

## Else statement

The `else` statement is used to run a block of code once the condition is no longer `True`. The `else` statement
is known as a control flow statement and is usually used in conjunction with other control flow statements such as the
`if`, `elif`, `try`, `except` and `finally`. _Find out more in respective segments_


```python
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
```

_After 5 iterations of the loop the `else` statement is executed and prints out its contents, this is a result of the `while` 
loops condition no longer being satisfied_

# For Loops

A `for` loop is used for iterating over a sequence of items. (`list`, `tuple`, `dictionary`, `set` or a `string`)

The `for` keyword is quite unique in Python compared to other programming languages. It works more like an iterator method as found in
other object-oriented programming languages, taking a sequence and outputting each item one by one as it iterates through the collection.

With a `for` loop we can execute a set of statements, once for each item in a `list`, `tuple`, `

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```

_Each of the items inside the fruits `list` will be printed out one-by-one_

_The `for` loop does not require an indexing variable to be set beforehand like other languages_

### Looping Through a String

Strings are what is known as an iterable object, this means they can be used within a `for` loop. The reason for this
is because technically a string is just a sequence of characters.

```python
for x in "banana":
  print(x)
```

_In this example the output will be each character in banana: `b` `a` `n` `a` `n` `a`_

## The Break Statement

The `break` statement can stop a loop before it has reached its pre-set amount of iterations. This can be useful
in situations when a certain value has been found in a sequence for example.

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
```

_The `break` statement has been told to execute if the current item in the list is equal to "banana". This happens in the
second iteration of the `for` loop meaning it won't print cherry._

## The continue statement

The `continue` statement can stop the current iteration of the loop, and continue with the next. More so in `for` loops
this statement is very useful as it can be used to stop certain iterations of the loop. For example, if a value
equals "banana" then `continue` to the next iteration of this `for` loop.

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
```

## The Range() Function

To loop through a set of code a specified number of times, we can use the `range()` function. This function takes 3 optional
arguments (`start`, `end`, `step`)

The `range()` function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default) and ends at a specified
number.

```python
for x in range(6):
    print(x)
```

_Note that range(6) is not the values of 0 to 6, but the values of 0 to 5_

_The reason for this is that the range will start at 0 by default and count to 6, not including the last number (6)_

The `range()` function default to 0 as a starting value, however as mentioned above it is possible to specify the starting value by adding a parameter:
`range(2, 6)`, which means values from 2 to 6 (but not including 6). `2`, `3`, `4`, `5`

```python
for x in range(2, 6):
  print(x)
```

The `range()` function defaults to increment by 1, however it is possible specify the increment value by adding a third parameter known as the step: `range(2, 30, 3)`.
This can be useful if you are going through a sequence that has a particular pattern you are aware of.

```python
for x in range(2, 30, 3):
  print(x)
```

## Else in For Loop

The `else` keyword `for` loop specifies a block of code to be executed when the loop is finished. Print all numbers from 0 to 5, and
print a message when the loop has ended.

```python
for x in range(6):
  print(x)
else:
  print("Finally finished!") 
```

## Nested Loops

A nested object is an object within another, this means that they will take place within the execution of the first object.
Here a nested loop is a loop inside a loop. The `inner loop` will be executed one time for each iteration of the `outer loop`.

```python
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 
```

_This is an excellent use of the for `nested loops` it will print each adj along with each fruit and repeat for each adjective._

## Pass Statement

`for` loops cannot be empty, but if you for some reason have a `for` loop that is perhaps a placeholder for a future functionality, put the
`pass` statement to avoid getting an error.

```python
for x in [0, 1, 2]:
  pass
```

_In my experience this is a very helpful keyword to layout your code before implementation, else it will be throwing errors all the time, 
which is both annoying and troublesome_

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



