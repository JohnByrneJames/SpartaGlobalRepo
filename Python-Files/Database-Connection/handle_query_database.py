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

    def create_cursor(self, connection):  # create cursor
        self.__cursor = connection.cursor()

    def load_database(self):
        self._load_database_structure(self.__cursor)  # Load database tables

    def refresh_cursor(self):  # refresh cursor, think it needs as it could cause errors
        self.establish_connection()

    # This was meant to be a query builder but it didn't work due to variable queries not being supporting in pyodbc
    def query_builder(self):
        try:
            table_to_select = input("Which table are you selecting?")
            column_to_select = input("Okay.. and what do you want to see type a column (case-sensitive) or type all: ")
            self.refresh_cursor()
            self.query_database(table_to_select, column_to_select, self.__cursor)
        except Exception:
            print("That column, doesn't exist.. if you forgot the names go back and load up the columns")

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

