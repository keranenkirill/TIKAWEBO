from sqlalchemy.sql import text
from db import db


def add_review(user_id, property_id, review_text):
    """
    Adds a new review to the database for a specific property by a user.

    Args:
        user_id (int): The ID of the user adding the review.
        property_id (int): The ID of the property being reviewed.
        review_text (str): The text content of the review.

    Returns:
        bool: True if the review was added successfully, False otherwise.

    Raises:
        Exception: If there is an error while adding the review.
    """
    try:
        sql = text("""
            INSERT INTO reviews (user_id, property_id, review)
            VALUES (:user_id, :property_id, :review)
        """)
        db.session.execute(sql, {
            'user_id': user_id,
            'property_id': property_id,
            'review': review_text
        })
        db.session.commit()
        return True
    except Exception as e:
        print(f"Error adding review: {e}")
        db.session.rollback()
        return False


def get_reviews_by_property(property_id):
    """
    Fetches all reviews for a specific property.

    Args:
        property_id (int): The ID of the property whose reviews are being fetched.

    Returns:
        list: A list of dictionaries containing reviews for the property, or an empty list if no reviews are found.

    Raises:
        Exception: If there is an error while fetching the reviews.
    """
    try:
        sql = text("""
            SELECT r.id, r.review, u.username
            FROM reviews r
            JOIN users u ON r.user_id = u.id
            WHERE r.property_id = :property_id
        """)
        result = db.session.execute(sql, {'property_id': property_id})
        return result.fetchall()
    except Exception as e:
        print(f"Error fetching reviews for property {property_id}: {e}")
        return []


def get_reviews_by_user(user_id):
    """
    Fetches all reviews made by a specific user.

    Args:
        user_id (int): The ID of the user whose reviews are being fetched.

    Returns:
        list: A list of dictionaries containing the user's reviews, or an empty list if no reviews are found.

    Raises:
        Exception: If there is an error while fetching the reviews.
    """
    try:
        sql = text("""
            SELECT r.id, r.review, p.title
            FROM reviews r
            JOIN properties p ON r.property_id = p.id
            WHERE r.user_id = :user_id
        """)
        result = db.session.execute(sql, {'user_id': user_id})
        return result.fetchall()
    except Exception as e:
        print(f"Error fetching reviews for user {user_id}: {e}")
        return []


def delete_review(review_id, user_id):
    """
    Deletes a review made by a user.

    Args:
        review_id (int): The ID of the review to be deleted.
        user_id (int): The ID of the user who made the review.

    Returns:
        bool: True if the review was successfully deleted, False otherwise.

    Raises:
        Exception: If there is an error during the deletion.
    """
    try:
        sql = text("""
            DELETE FROM reviews
            WHERE id = :review_id AND user_id = :user_id
        """)
        db.session.execute(sql, {'review_id': review_id, 'user_id': user_id})
        db.session.commit()
        return True
    except Exception as e:
        print(f"Error deleting review {review_id}: {e}")
        db.session.rollback()
        return False
