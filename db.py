"""
This module sets up the database connection using SQLAlchemy for a Flask application.
It also checks if the database exists and creates it using the `schema.sql` file if necessary.

Classes:
    None

Functions:
    check_database_exists() -> bool
        Checks if the database exists by running a simple SQL query.
        Returns True if the database exists, otherwise False.

    create_database() -> None
        Executes the SQL statements in `schema.sql` to create the database and tables
        if the database does not exist.

    init_db(app: Flask) -> None
        Configures the database connection and initializes the SQLAlchemy app.
        If the database does not exist, it creates the database first.
        
Variables:
    db (SQLAlchemy): An instance of SQLAlchemy used for database operations.
    SCHEMA_FILE (str): The path to the SQL file used to initialize the database schema.
"""

from flask_sqlalchemy import SQLAlchemy
from os import getenv
from sqlalchemy import create_engine, text
import os

# Initialize SQLAlchemy
db = SQLAlchemy()

# Path to the SQL schema file
SCHEMA_FILE = "schema.sql"


def check_database_exists():
    """
    Checks if the database exists by running a simple SQL query.

    If the database does not exist, it will trigger the schema.sql file to create the 
    database and its tables.

    Returns:
        bool: True if the database exists, False otherwise.
    """
    database_url = getenv("DATABASE_URL")
    engine = create_engine(database_url)

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print()
        print("DATABASE EXISTS.")
        return True
    except Exception:
        print()
        print("DATABASE NOT FOUND.")
        return False


def create_database():
    """
    Executes the SQL statements in `schema.sql` to create the database and tables
    if the database does not exist.
    """
    database_url = getenv("DATABASE_URL")
    engine = create_engine(database_url)

    try:
        with open(SCHEMA_FILE, 'r') as file:
            schema_sql = file.read()
            with engine.connect() as connection:
                connection.execute(text(schema_sql))
        print()
        print("DATABASE AND TABLES CREATED SUCCESFULLY.")
    except Exception as e:
        print()
        print(f"ERROR CREATING THE DATABASE: {e}")


def init_db(app):
    """
    Configures the database connection and initializes the SQLAlchemy app.

    If the database does not exist, it first creates the database using `schema.sql`.

    Args:
        app (Flask): The Flask application instance.
    """

    if check_database_exists():
        print()
        print("THE DATABASE ALREADY EXISTS, CONTINUING WITH INITIALIZATION.")
    else:
        create_database()
        print()
        print("THE DATABASE HAS BEEN CREATED SUCCESSFULLY.")

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")

    db.init_app(app)
