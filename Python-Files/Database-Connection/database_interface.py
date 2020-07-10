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
