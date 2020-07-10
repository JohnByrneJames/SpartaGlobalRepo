import pyodbc

class DatabaseConnector:
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

    def establish_connection(self):
        connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=" \
                           + self.__server + ";DATABASE=" + self.__database + \
                           ";UID=" + self.__username + ";PWD=" + self.__password
        self.__connection_string = connection_string

        try:
            with pyodbc.connect(self.__connection_string, timeout=5) as connection:
                # Success and connection has been made
                print("-" * 20 + """\nConnection has been made ~ :)\n""" + "-" * 20 + "\n")
        except (ConnectionError, pyodbc.OperationalError, pyodbc.DatabaseError):
            print("connection has timed out, or the database was not available")
        except pyodbc.InterfaceError:
            print("Invalid connection to DB interface")
        else:
            # The cursor is a control structure, here it gets the cursor and stores it in a class attribute
            self.create_cursor(connection)

    def create_cursor(self, connection):
        self.__cursor = connection.cursor()
        self.query_database()

    def query_database(self):
        for table in self.__cursor.tables():  # Search through tables
            if table.table_schem != "dbo":  # not a database table - escape
                break
            else:  # get columns
                print(table.table_name)

        # Create loop to ask user for input



