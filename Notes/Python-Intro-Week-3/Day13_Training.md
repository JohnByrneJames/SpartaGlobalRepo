###### Sparta Global Training Day 13
###### Python starting...
___

> 9:00 AM Stand-up [Morning]

Yesterday was good, I learned a lot about what makes a good profile for the clients to view and why
it is important to work hard in making an attractive and summarise yourself to attract them. Python 
variables is nothing new to me and they are very similar to other languages like C#, C++, Java and JavaScript.

**Blockers..** I have no blockers from yesterday. 

**Question** : In Python, a variable must be declared before it is assigned a value.
<br>**Answer** : Variables need not be declared or defined in advance in Python. To create a variable, you just assign it a value

We are done, now to the [**Trello**](https://trello.com/b/eZdQiVQU/engineering-67) board to update the Week Sprint and Doing/ Done.

* **Today's Objectives**
    * **Data Types**
    * **Lists and Tuples**
    * **Concatenation**
    
___

> 10:15 AM Python Variables, Data types and operators [Mid-Morning]
    
## Data Types and Operators

| Operand | Description                                                | Example |
|---------|------------------------------------------------------------|---------|
| **>**       | True if left operand is greater than the right             | x > y   |
| **<**       | True if left operand is less than the right                | x < y   |
| **==**      | True if both operands are equal                            | x == y  |
| **!=**      | True if both operands are qual                             | x != y  |
| **>=**      | True if left operand is greater than or equal to the right | x >= y  |
| **<=**      | True if left operand is less than or equal to the right    | x <= y  |
Here we are comparing the two variables, therefore it will return `FALSE` because **10** is not equal to **11**.
```python
x = 10 
y = 11 

print(x == y)
```

Here we are comparing two variables, therefore it will return `TRUE` because **10** is not equal to **11**.
```python
x = 10
x = 11

print(x != y)
```

... The rest are quite straight forward... and can be found in greater detail in my [**Python Cheatsheet**](W3Schools-Python-CheatSheet.md)


## Strings and Casting

| Function   | Description                                                             | Example                     |
|------------|-------------------------------------------------------------------------|-----------------------------|
| **len**        | Returns the length of a string                                          | len(string)                 |
| **count**      | Returns the amount of times a string appears in another string          | string.count('t')           |
| **lower**      | Converts a string to all lower case                                     | string.lower()              |
| **upper**      | Converts a string to all Upper case                                     | string.upper()              |
| **title**      | Converts the letter of each word in a string to a capital               | string.title()              |
| **capitalize** | Converts the first letter in a string to a capital                      | string.capitalize()         |
| **replace**    | Replace text in a string with the string specified                      | string.replace('text', 't') |
| **startswith** | Returns either True or False if the string starts with the given string | string.startswith('t')      |

If the movie is a alphanumeric rating it will convert it to a number

> **~ Today's Python Files ~** <br>
* [**variables**](../../Python-Files/Revision-Files/variables.py) :page_with_curl:

* [**operators**](../../Python-Files/Revision-Files/operators.py) :page_with_curl:

* [**string_casting**](../../Python-Files/Revision-Files/strings.py) :page_with_curl:

* [**lists**](../../Python-Files/Revision-Files/lists.py) :page_with_curl:

* [**tuples**](../../Python-Files/Revision-Files/tuples.py) :page_with_curl:

* [**control_flow**](../../Python-Files/Revision-Files/control_flow.py) :page_with_curl:

* [**dictionaries**](../../Python-Files/Revision-Files/dictionaries.py) :page_with_curl:

* [**loops**](../../Python-Files/Revision-Files/loops.py) :page_with_curl:

* [**sets**](../../Python-Files/Revision-Files/sets.py) :page_with_curl:

* [**while_loops**](../../Python-Files/Revision-Files/while_loop.py) :page_with_curl:

___
**Homework**
* Do dictionaries exercise at bottom of [**loops.py**](/Python-Files/Revision-Files/loops.py)
