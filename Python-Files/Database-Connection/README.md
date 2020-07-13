###### Python Project - Using OOP work with the database connection and create a user-friendly application.
###### This doesn't have to be 100% perfect but demonstrate the OOP and database concepts you have learnt in the past two weeks of Python.

___

# Contents
- [x] [Concept and Ideas :art:](#concepts-and-ideas)

- [x] [Implementation :zap:](#implementation)

- [x] [Important Points :bookmark:](#important-points)

- [x] [Future Improvements :construction_worker:](#future-improvements)

___

# Concepts and Ideas

This was created at the end of the fourth week, it was a chance for us to show to Astha what we had achieved and learnt
over the past weeks. We had just learnt more about databases, read and write permissions, API and exception handling. However
my plan for this was to include concepts that I wanted to showcase as I have programmed before and understand a lot of concepts
but this was to reinforce those.

## Concept

At first I wanted to create a function that took into the credentials for the database, logged in the user and using read/ write
permissions created a .txt file that would store their user information. This would create a stateful class as it could actually read that file
again if the user was to log in again. I also wanted to add the functionality for the user to dynamically query to database
from a users point of view, this would then be put into a query and passed into the `execute()` method. This was not possible as I tried
many different combinations but none seem to work, this is actually not working in the final product but I left it to display my thought process.

### Final Structure

```json
├── database_interface.py
└───┬ handle_query_database.py (Inherits handle_table_column)
    ╠══ establish_connection(self)
    ╠══ create_cursor(self, connection)
    ╠══ load_database(self)
    ╠══ refresh_cursor(self)
    ╠══ query_builder(self)
    ╠══ user_interface(self)
    └─┬ handle_table_column.py (abstract)
      ╠══ _load_database_structure(self, cursor)
      ╠══ create_table_string(self)
      ╠══ create_column_string(self, table_name)
      ╠══ query_database(self, table_name, column_name, cursor)
      ╠══ get_average_of_product(cursor)
```

The `database_interface.py` is the file where the instance is made, along with the correct credentials which are aliased
through the `os` module. The calls to the initial method is also made which is actually designed to flow through the
program and set up all the relevant functionality.

Above is the structure of the overall program, it is quite small but has two classes, one is more of a front-facing derived
class which inherits from the parent to take advantage of its methods, this is a slight form of abstraction as it allows
the messy process to be hidden.

# Implementation

## Program frontend

So the first thing I needed to do was make it a little more secure by making the database login details private to anyone who
may look at the GitHub, to do this the `os` module was used. To do this I created 4 new system environment variables on my computer.
These could then be referenced to via the program, using the name of the variables that were set, the great thing about this is that it
will only work on my personal computer and adds a layer of security to the credentials. 

```python
from handle_query_database import DatabaseConnector
import os

# Connection credentials
server = os.environ.get("db_server")  # Server name, this here gets the OS private environment variables
database = os.environ.get("db_database")  # Database name, this here gets the OS private environment variables
# Database Login credentials
username = os.environ.get("db_username")  # username, this here gets the OS private environment variables
password = os.environ.get("db_password")  # password, this here gets the OS private environment variables

db_instance = DatabaseConnector(server, database, username, password)  # create instance with credentials

db_instance.establish_connection()  # create a connection in the instance
db_instance.user_interaction()
```

The `DatabaseConnector` class was also imported from `handle_query_database.py`, this allows an instance to be created and
as a result calls could be made to the classes methods.

## Program backend

The `handle_query_database.py` file handled the programs main functionality and made use of the `handle_table_column.py` file
to do all the cumbersome database operations and return only the results. It is favourable this way as it reduces the amount of code that
is written in a single class and also allows each method to have a specific functionality.

### Database Connector Initialisation

```python
from handle_table_column import TableInterface
import pyodbc
import time

class DatabaseConnector(TableInterface):
    __server = None
    __database = None
    __username = None
    __password = None
    __connection_string = None
    __cursor = None

    def __init__(self, server, database, username, password):
        self.__server = server
        self.__database = database
        self.__username = username
        self.__password = password
        super().__init__()  # Inheriting class before
```

First the relevant class is imported to enable inheritance between the two and then, `pyodbc` is imported to allow querying of the
database and lastly I included `time` as it is quite nice to use when working in the terminal to create satisfying delays between operations (purely aesthetic).

So the program works by first declaring some essential attributes of the class, these are then applied where needed in the classes
initialisation function, settings the `database`, `server`, `username` and `password` attributes which are all private. After that the
`super()` method is used to inherit any methods and attributes from the parent class.

These are the credentials required to access the database, this will then go into the `establish_connection()` method which is the
part of the class which establishes a connection to the database. There is also exception handling in place here incase any problems occur, this will
return them out of the class and tell them the specific error encountered.

### Establishing a connection to the database

```python
    def establish_connection(self):  # establishing connection
        connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=" \
                           + self.__server + ";DATABASE=" + self.__database + \
                           ";UID=" + self.__username + ";PWD=" + self.__password
        self.__connection_string = connection_string

        try:
            with pyodbc.connect(self.__connection_string, timeout=5) as connection:  # Connection to database
                # Success and connection has been made
                print("-!" * 20 + """\nGetting connection...\n""" + "-!" * 20 + "\n")
        except (ConnectionError, pyodbc.OperationalError, pyodbc.DatabaseError):
            print("connection has timed out, or the database was not available")
            return
        except pyodbc.InterfaceError:
            print("Invalid connection to DB interface")
            return
        else:
            # The cursor is a control structure, here it gets the cursor and stores it in a class attribute
            self.create_cursor(connection)  # create a connection
            self.load_database()  # load database
```  

If the connection is made successfully then the user will "connection made" message in order to inform them of the success. After that
the class uses the self method to call the `create_cursor(connection)` method it will establish a connection inside that method,
then store that connection A.K.A the `cursor` in the classes attribute. After that the `load_database()` method will be called
which will call an inherited method called `load_database_structure(self.cursor)`  

### Loading the the tables and their columns

```python
class TableInterface:
    _database_tables_columns = {}
    _cursor_tables = []

    def __init__(self):
        pass

    def _load_database_structure(self, cursor):
        self._database_tables_columns.clear()  # Removes all items from the list

        print("Reading Tables and Columns in Database...")
        time.sleep(2)

        for line in cursor.tables():
            self._cursor_tables.append(line)
        for table in self._cursor_tables:  # Search through tables
            if table.table_schem != "dbo":  # not a database table - escape
                break
            else:  # {table_name: {Column_name: data_type, column_name: data_type}, table
                self._database_tables_columns[table.table_name] = {}
                for column in cursor.columns(table.table_name):
                    self._database_tables_columns[table.table_name][column.column_name] = column.remarks

```

This is the inside the `handle_table_column.py` file where the `TableInterface` class is defined and has various methods that are
designed to specifically carry out one task. This code is a little confusing but what is does generally is
define a `dictionary` to store tables with a nested `dictionary` as its value, and that nested `dictionary` has a value of the
`column_name` and a value of its `column.remarks` which is just a placeholder at this point.

First of all the tables are stored in a simple `list`. This list is used in the next part of the code, here a for loop iterates over the
`list`, getting the tables name and going into a further for loop which iterates over the columns in a table, using the table name and the
cursor to create a connection. This is then constructed into a `dictionary` within a `dictionary`. This is a dynamic implementation as it will scale or descale as more tables, and columns are
added to the database. There is also the part that checks the see if the `table_schem` is equals to dbo, this tells the for loop to
break when the table being iterated isn't a database object e.g. not a table.

### User Interaction Handling

```python
    def user_interaction(self):  # user interaction
        print("Welcome!.. ", self.__username, self.__database, "was loaded successfully")

        users_exit_status = False  # It is good practice to control the while loop with a variable that can be altered
        users_help = "\nInstructions:\n" + "To view tables type [T]\n" + "To start a query type [S]\n" +\
                     "To exit type [E]\n" + "To get help type [H]\n" + "To get products average [A]\n"
        print(users_help)

        while not users_exit_status:
            users_input = input("What would you like to do? ")

            if users_input.lower() == "t":
                print("Loading tables...\n")
                #  time.sleep(1)
                print(self.__database + " Tables. \n")
                print(self.create_table_string())
                try:
                    users_input = input("Enter a table to see its columns (Include capitals) ")
                    if len(users_input) is 0:
                        raise ValueError
                    print("Loading columns...\n")
                    print(users_input + " Columns. \n")
                    print(self.create_column_string(users_input))
                except ValueError:
                    print("That column doesn't exist\n")
                except Exception:
                    print("Unexpected error!\n")
                finally:
                    print("Restarting... \n" + "*"*20 + "\n")
                    time.sleep(1)

            elif users_input.lower() == "s":  # if they type s go here
                self.query_builder()

            elif users_input.lower() == "e":  # exit
                print("\nExiting program, see you next time...")
                time.sleep(1)
                print("\nSaving your database for future use")
                users_exit_status = True

            elif users_input.lower() == "a":  # get average password
                self.refresh_cursor()
                print("\ncalculating average of product price\n")
                TableInterface.get_average_of_product(self.__cursor)
                time.sleep(1)

            elif users_input.lower() == "h":
                print(users_help)
            else:
                print("\nSorry " + users_input.__str__() + " is not a recognised command")
```

Once the database has been successfully loaded into the variables in the parent class holding the names of the columns and tables,
it then goes into a method called `user_interaction()`. This method uses a while loop and control flow statements to give the user
various options such as loading all the tables in the database and then the chance to load all the columns in that table. They can also
reprint the help text with `h`, exit with `e`, get the average of the products with `a` and start a query with `s` although at the moment
this is not properly implemented. 

The user will remain in this while loop as it is set to `not users_exit_status` and only exit once they enter the `e` which will escape the while loop
by setting it to True which will no longer meet the condition of the loop.

```python
    @staticmethod
    def get_average_of_product(cursor):
        query = cursor.execute("SELECT UnitPrice FROM Products")

        rows = query

        prices = []

        for row in rows:
            prices.append(row[0])

        # print("Average of products are £", round(sum(prices) / len(prices), 2))

        average = round(statistics.mean(prices), 2)

        print(average)
```

The two statements that print out the tables and columns are quite generic and can be viewed in the files in this directory.
However for the average I wanted to point out that I first queried the database for all the `UnitPrice` attributes and then
added them into a list and applied the `mean()` function which is available through the `statistics` module. This is one of two ways
however it is a nice way to quickly get the result making the most of the modules available in python.

# Important Points

* It is important to make sure you keep your private credentials such as the ones used to access the database private. This can be done by
adding the connection file to the `.gitignore` or like I did creating system environment variables that can be accessed through the os module.

* When printing out database tables it is important that you check for the `"dbo"` table_schem as this is a table, the other
data structures returned are other pieces of less informative memory.
* The best way to create a dynamic program is to make methods that are segregated and perform typically one and only one functionality. This is also used when
the tables and columns are stored in a dictionary as it loops through the variables created on connection ensuring data integrity.
* Sometimes the `Cursor` object is a little flaky and can return incorrect data if used in quick succession or nested functions, for this reason I first
gathered the tables and stored them in a separate list and then using that list I then used the cursor to get the relevant columns.
* When working with users or operations that are not straight-forward yes or no responses it is imperative that you include exception handling. This allows the user to
be more informed about what mistake they have made and also protect the program from failing during operation.

# Future improvements

For this program I was pretty happy with the outcome, although it is not everything I first imagined, to keep this short I have summarised
the improvements in bullet points.
* Addition of stateful text files that can remember a user when they logged onto the database before, and actively retrieve their information if they enter
their username and password correctly.

* Figure out how a query builder can be created that works, this is important because asking the user to directly enter a query is both inefficient and
bad practice as they wont know how to query, therefore asking them what they want in layman terms is important and provides ease-of-use.
* More exceptions added for each of the stages so that the user can be more informed of error details and also it is a better design methodology.

I also did a separate project which allowed the user to add in their favorite food, this would then be written to a temporary text file
which tracks the latest additions, and another permanent text file which tracks the history of the additions into the lists including any errors that
have been encountered. If you are interest in seeing that, you can find it [**HERE**](../Exercise-Files/Rasing-Exception)