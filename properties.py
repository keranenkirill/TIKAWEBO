from sqlalchemy.sql import text
from db import db


def add_property(title, price, description, image_url, user_id):
    """
    Adds a new property to the database.

    Args:
        title (str): The title of the property.
        price (float): The price of the property.
        description (str): A description of the property.
        image_url (str): The filename of the property image.
        user_id (int): The ID of the user who listed the property.

    Raises:
        Exception: If there is an error adding the property to the database.
    """
    try:
        sql = text("""
            INSERT INTO properties (title, price, description, image_url, user_id)
            VALUES (:title, :price, :description, :image_url, :user_id)
        """)
        db.session.execute(sql, {
            "title": title,
            "price": price,
            "description": description,
            "image_url": image_url,
            "user_id": user_id
        })
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error adding property: {e}")


def get_property_by_id(property_id):
    """
    Retrieves a property by its ID.

    Args:
        property_id (int): The ID of the property.

    Returns:
        dict or None: The property record if found, or None if not found.

    Raises:
        Exception: If there is an error fetching the property.
    """
    try:
        sql = text("SELECT * FROM properties WHERE id=:property_id")
        result = db.session.execute(sql, {"property_id": property_id})
        return result.fetchone()
    except Exception as e:
        print(f"Error fetching property: {e}")
        return None


def get_all_properties():
    """
    Retrieves all properties from the database.

    Returns:
        list: A list of all properties.

    Raises:
        Exception: If there is an error fetching the properties.
    """
    try:
        sql = text("SELECT * FROM properties")
        result = db.session.execute(sql)
        return result.fetchall()
    except Exception as e:
        print(f"Error fetching all properties: {e}")
        return []


def get_properties_by_user(user_id):
    """
    Retrieves all properties listed by a specific user.

    Args:
        user_id (int): The ID of the user.

    Returns:
        list: A list of properties listed by the user.

    Raises:
        Exception: If there is an error fetching the properties.
    """
    try:
        sql = text("SELECT * FROM properties WHERE user_id=:user_id")
        result = db.session.execute(sql, {"user_id": user_id})
        return result.fetchall()
    except Exception as e:
        print(f"Error fetching properties by user: {e}")
        return []


def get_user_listed_properties(user_id):
    """
    Fetches all properties listed by a specific user.

    Args:
        user_id (int): The ID of the user.

    Returns:
        list: A list of properties listed by the user.
    """
    query = text("""
    SELECT id, title, price, description, image_url
    FROM properties
    WHERE user_id = :user_id;
    """)
    result = db.session.execute(query, {'user_id': user_id}).fetchall()
    print("USER LISTED PROPERTIES:", result)
    return result


def get_user_rented_properties(user_id):
    """
    Fetches all properties rented by a specific user.

    Args:
        user_id (int): The ID of the user.

    Returns:
        list: A list of rented properties with booking details.
    """
    sql = text("""
    SELECT properties.title, properties.price, properties.description, properties.image_url, 
           bookings.start_date, bookings.end_date, bookings.id AS booking_id
    FROM bookings
    JOIN properties ON bookings.property_id = properties.id
    WHERE bookings.user_id = :user_id;
    """)
    return db.session.execute(sql, {'user_id': user_id}).fetchall()


def get_rented_properties(user_id):
    """
    Retrieves all properties rented by a specific user.

    Args:
        user_id (int): The ID of the user.

    Returns:
        list: A list of rented properties including booking details.
    """
    sql = text("""
        SELECT p.title, p.price, p.description, p.image_url, b.id as booking_id, b.start_date, b.end_date
        FROM bookings b
        JOIN properties p ON b.property_id = p.id
        WHERE b.user_id = :user_id
    """)
    result = db.session.execute(sql, {'user_id': user_id})
    return result.fetchall()


def delete_booking(booking_id, user_id):
    """
    Deletes a booking made by a user.

    Args:
        booking_id (int): The ID of the booking to be deleted.
        user_id (int): The ID of the user who made the booking.

    Returns:
        bool: True if the booking was successfully deleted, False otherwise.

    Raises:
        Exception: If there is an error deleting the booking.
    """
    print("BOOKING ID:", booking_id, user_id)
    try:
        sql = text("""
            DELETE FROM bookings
            WHERE id = :booking_id AND user_id = :user_id
        """)
        db.session.execute(sql, {'booking_id': booking_id, 'user_id': user_id})
        db.session.commit()
        return True
    except Exception as e:
        print(f"Error deleting booking: {e}")
        db.session.rollback()
        return False


def get_bookings_by_property_id(property_id):
    """
    Retrieves all bookings for a specific property.

    Args:
        property_id (int): The ID of the property.

    Returns:
        list: A list of bookings for the property, including booking details.

    Raises:
        Exception: If there is an error fetching the bookings.
    """
    try:
        sql = text("""
            SELECT  b.user_id, u.username, b.start_date, b.end_date
            FROM bookings b
            JOIN users u ON b.user_id = u.id
            WHERE b.property_id = :property_id
        """)
        result = db.session.execute(sql, {"property_id": property_id})
        return result.fetchall()
    except Exception as e:
        print(f"Error fetching bookings by property ID: {e}")
        return []


def delete_property(property_id, user_id):
    """
    Deletes a property listed by a user.

    Args:
        property_id (int): The ID of the property to be deleted.
        user_id (int): The ID of the user who listed the property.

    Returns:
        bool: True if the property was successfully deleted, False otherwise.

    Raises:
        Exception: If there is an error deleting the property.
    """
    try:
        sql = text("""
            DELETE FROM properties
            WHERE id = :property_id AND user_id = :user_id
        """)
        db.session.execute(
            sql, {'property_id': property_id, 'user_id': user_id})
        db.session.commit()
        return True
    except Exception as e:
        print(f"Error deleting property: {e}")
        db.session.rollback()
        return False


def book_property(user_id, property_id, start_date, end_date):
    """
    Creates a booking for a property by a user.

    Args:
        user_id (int): The ID of the user making the booking.
        property_id (int): The ID of the property to be booked.
        start_date (datetime): The start date of the booking.
        end_date (datetime): The end date of the booking.

    Raises:
        Exception: If there is an error creating the booking.
    """
    try:
        sql = text("""
            INSERT INTO bookings (user_id, property_id, start_date, end_date)
            VALUES (:user_id, :property_id, :start_date, :end_date)
        """)
        db.session.execute(sql, {
            'user_id': user_id,
            'property_id': property_id,
            'start_date': start_date,
            'end_date': end_date
        })
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error booking property: {e}")


def get_user_bookings(user_id):
    """
    Retrieves all bookings made by a specific user.

    Args:
        user_id (int): The ID of the user.

    Returns:
        list: A list of bookings made by the user.

    Raises:
        Exception: If there is an error fetching the bookings.
    """
    try:
        sql = text("""
            SELECT * FROM bookings
            WHERE user_id=:user_id
        """)
        result = db.session.execute(sql, {"user_id": user_id})
        return result.fetchall()
    except Exception as e:
        print(f"Error fetching bookings: {e}")
        return []
