###### Python Project - Using OOP work with the database connection and create a user-friendly application.
###### This doesn't have to be 100% perfect but demonstrate the OOP and database concepts you have learnt in the past two weeks of Python.

___

## Contents
- [ ] [Concept and Ideas :art:](#concepts-and-ideas)

- [ ] [Implementation :zap:](#implementation)

- [ ] [Important Points :bookmark:](#important-points)

- [ ] [Future Improvements :construction_worker:](#future-improvements)

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

First of all the tables are stored in a simple `list`,  

