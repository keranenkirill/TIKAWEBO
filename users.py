from sqlalchemy import text
from sqlalchemy.sql import text
from db import db


def login(username):
    """
    Fetches the user's ID and hashed password from the database based on the username.

    Args:
        username (str): The username of the user trying to log in.

    Returns:
        dict or None: A dictionary containing the user's ID and hashed password if found, 
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

    Args:
        username (str): The username to check in the database.

    Returns:
        dict or None: A dictionary containing the user's ID if the user exists,
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

    Args:
        user_id (int): The ID of the user.

    Returns:
        dict or None: A dictionary containing the user's email and phone if found,
                      otherwise None.

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


def update_user_profile(user_id, email, phone, password):
    """
    Updates the user's profile information in the database.

    Args:
        user_id (int): The ID of the user whose profile is being updated.
        email (str): The new email address for the user.
        phone (str): The new phone number for the user.
        password (str): The new password for the user.

    Returns:
        bool: True if the profile was successfully updated, False otherwise.

    Raises:
        Exception: If there is an error during the profile update.
    """
    try:
        sql = text(
            "UPDATE user_profiles SET email=:email, phone=:phone WHERE user_id=:user_id")
        db.session.execute(
            sql, {"email": email, "phone": phone, "user_id": user_id})

        sql_password = text(
            "UPDATE users SET password=:password WHERE id=:user_id")
        db.session.execute(
            sql_password, {"password": password, "user_id": user_id})

        db.session.commit()
        return True
    except Exception as e:
        print(f"Error updating user profile: {e}")
        db.session.rollback()
        return False


def add_new_user(psswd1, username, email, phone):
    """
    Adds a new user to the database after checking that the username does not already exist.
    The password is hashed before storing it in the database.

    Args:
        psswd1 (str): The plain-text password to be hashed and stored.
        username (str): The username of the new user.
        email (str): The email of the new user.
        phone (str): The phone number of the new user.

    Returns:
        int or None: The ID of the newly added user if successful, or None if the username 
                     already exists or if there is an error during the operation.

    Raises:
        Exception: If there is an error during the user creation process.
    """
    if check_user_in_db(username):
        print("Username already exists!")
        return None
    try:
        sql = text(
            "INSERT INTO users (username, password) VALUES (:username, :password) RETURNING id")
        result = db.session.execute(
            sql, {"username": username, "password": psswd1})

        new_user_id = result.fetchone()[0]  # Fetch the returned user ID

        sql_profile = text(
            "INSERT INTO user_profiles (user_id, email, phone) VALUES (:user_id, :email, :phone)")
        db.session.execute(
            sql_profile, {"user_id": new_user_id, "email": email, "phone": phone})

        db.session.commit()
        return new_user_id
    except Exception as e:
        print(f"Error adding new user: {e}")
        db.session.rollback()
        return None


def delete_user_related_data(user_id):
    try:
        sql = text("""
            DELETE FROM reviews
            WHERE property_id IN (SELECT id FROM properties WHERE user_id=:user_id)
        """)
        db.session.execute(sql, {"user_id": user_id})

        sql = text("DELETE FROM user_profiles WHERE user_id=:user_id")
        db.session.execute(sql, {"user_id": user_id})

        sql = text("DELETE FROM properties WHERE user_id=:user_id")
        db.session.execute(sql, {"user_id": user_id})

        sql = text("DELETE FROM users WHERE id=:user_id")
        db.session.execute(sql, {"user_id": user_id})

        db.session.commit()
        return True

    except Exception as e:
        print(f"Error deleting user data: {e}")
        db.session.rollback()
        return None
