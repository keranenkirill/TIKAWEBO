from werkzeug.security import generate_password_hash
from sqlalchemy.sql import text
from db import db


def login(username):
    """
    Fetches the user's ID and hashed password from the database based on the username.

    Parameters:
        username (str): The username of the user trying to log in.

    Returns:
        result (dict or None): A dictionary containing the user's ID and hashed password if found, 
        otherwise None.

    Raises:
        Exception: If there is an error during the login query.
    """
    try:
        sql = text("SELECT id, password FROM users WHERE username=:username")
        result = db.session.execute(sql, {"username": username})
        return result.fetchone()
    except Exception as e:
        print(f"Error during login: {e}")
        return None


def check_user_in_db(username):
    """
    Checks if a user with the given username exists in the database.

    Parameters:
        username (str): The username to check in the database.

    Returns:
        result (dict or None): A dictionary containing the user's ID if the user exists,
        otherwise None.

    Raises:
        Exception: If there is an error while checking the user in the database.
    """
    try:
        sql = text("SELECT id FROM users WHERE username=:username")
        return db.session.execute(sql, {"username": username}).fetchone()
    except Exception as e:
        print(f"Error checking user in DB: {e}")
        return None


def get_userprofile_by_id(user_id):
    """
    Retrieves the user profile (email and phone) for a specific user by their ID.

    Parameters:
        user_id (int): The ID of the user.

    Raises:
        Exception: If there is an error fetching the user profile.
    """
    try:
        sql = text(
            "SELECT email, phone FROM user_profiles WHERE user_id=:user_id")
        result = db.session.execute(sql, {"user_id": user_id})
        profile = result.fetchone()
        return profile

    except Exception as e:
        print(f"Error fetching user profile for user {user_id}: {e}")
        return None


def add_new_user(psswd1, username):
    """
    Adds a new user to the database after checking that the username does not already exist.
    The password is hashed before storing it in the database.

    Parameters:
        psswd1 (str): The plain-text password to be hashed and stored.
        username (str): The username of the new user.

    Returns:
        bool: True if the user is successfully added, False if the username already exists or
        if there is an error during the operation.

    Raises:
        Exception: If there is an error during the user addition process.
    """
    if check_user_in_db(username):
        print("Username already exists!")
        return False
    try:
        hash_value = generate_password_hash(psswd1)
        sql = text(
            "INSERT INTO users (username, password) VALUES (:username, :password)")
        db.session.execute(sql, {"username": username, "password": hash_value})
        db.session.commit()
        return True
    except Exception as e:
        print(f"Error adding new user: {e}")
        db.session.rollback()
        return False
