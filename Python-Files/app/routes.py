from app import app
from flask import Flask, render_template, redirect, url_for, request


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

# The view function is actually pretty simple, it just returns a greeting card as a string. The two strange
# '@app.route' are decorators, these modify the function that follows it. A common pattern with decorators is to use
# them to register functions as callbacks for certain events. In this case, the @app.route decorator creates an
# association between the URL given as an argument and the function. In this example there are two decorates,
# which associate the URLs '/' and '/index' to this function. This means that when a web browser requests either
# of these two URLs, Flask is going to invoke this function and pass the return value of it back to the browser
# response. This is not clear at the moment, not until you run the application. To do this we need a top-level Python
# script that defines the Flask application instance. Let's call this script microblog.py. Then import the app
# instance.
