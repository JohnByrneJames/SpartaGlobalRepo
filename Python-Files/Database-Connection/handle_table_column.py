import pyodbc
import time
import statistics

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

    def create_table_string(self):
        counter = 0
        tables = ""
        for table in self._cursor_tables:
            if table.table_schem != "dbo":  # not a database table - escape
                break
            if counter == 4:
                tables += "\n"
                counter = 0
            tables += "  [" + table.table_name + "]  "
            counter += 1
        return tables

    def create_column_string(self, table_name):
        counter = 0
        column_names = ""

        for column in self._database_tables_columns[table_name]:
            if counter == 4:
                column_names += "\n"
                counter = 0
            column_names += " [" + column + "] "
            counter += 1

        return column_names

    def query_database(self, table_name, column_name, cursor):
        if column_name.lower() == "all":
            column_name = "*"

        query_to_execute = cursor.execute()

        rows = query_to_execute.fetchall

        for row in rows:
            print(row)

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