from flask import Flask

app = Flask(__name__)

from app import routes

# This creates the application object as an instance of the class flask imported from the flask package.
# The __name__ variable is passed to the Flask class is a Python predefined variable, which is set to the name of the
# in which it is used.

# After loading appropriate resources, the app imports the routes module, which doesn't yet exist. The app variable is
# defined as an instance of class Flask in the __init__.py script, which makes it a member of the app package.

# The bottom import for routes is a work around to circular imports, a common problem with Flask applications.
# You are going to see that the routes module needs to import the app variable defined in this script,
# so putting one of the reciprocal imports at the bottom avoids the error that results from the mutual
# references between these two files.

# The routes module is the routes of different URLs that the application implements. In Flask, handlers for the
# application routes are written as Python functions, called view functions. View functions are mapped to one or more
# route URLS - so that Flask knows what logic to execute when a client requests a given URL.

# To run the first version of the application, you need to set the FLASK_APP environment variable.
# This is done with:
# >>> $ set FLASK_APP=microblog.py
