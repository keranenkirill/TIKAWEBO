from flask import Flask
from db import init_db
from user_routes import init_user_routes
from property_routes import init_property_routes
from os import getenv

"""
This module sets up and runs the Flask application.

Functions:
    None

Variables:
    app (Flask): The Flask application instance.

Usage:
    This script initializes the Flask application, sets up the database connection,
    and registers the user and property routes. It also sets the secret key for the
    application from environment variables.

Attributes:
    app (Flask): The Flask application instance.
    app.secret_key (str): The secret key for the Flask application, retrieved from environment variables.
"""

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

init_db(app)

init_user_routes(app)
init_property_routes(app)

if __name__ == "__main__":
    app.run()
