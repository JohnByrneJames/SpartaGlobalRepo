# The Flask application instance is called app and is a member of the app package
# This looks confusing but you can rename the package or the variable to something else. (app directory) and __init__.py


# 'FLASK_APP=microblog.py' sets the microblog python
# I had to do the command `set FLASK_ENV=development' to make the flask app work, it doesn't run in the production
# environment.

from app import app

