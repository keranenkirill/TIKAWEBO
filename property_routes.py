from flask import render_template, request, session, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
import properties
from datetime import datetime

# Assuming you have a folder for uploaded images
UPLOAD_FOLDER = 'static/images/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # 2 MB limit for file uploads


def allowed_file(filename):
    """
    Checks if the provided file has an allowed extension (png, jpg, jpeg).
    Returns True if the file extension is allowed, otherwise False.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def init_property_routes(app):
    """
    Initializes all property-related routes for the Flask application.
    Handles property creation, bookings, property details, and deletion of bookings.
    """

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

    @app.route("/newlisting")
    def newlisting():
        """
        Route to display the form for creating a new property listing.
        Ensures that the user is logged in; otherwise, redirects to the login page.
        """
        if 'user_id' not in session:
            return redirect("/loginview")
        return render_template("newlisting.html")

    @app.route("/createlisting", methods=["POST"])
    def createlisting():
        """
        Route to handle the form submission for creating a new property listing.
        Validates the uploaded image and other details, then adds the new property
        to the database. If any validation fails, an error message is displayed.
        """
        if 'user_id' not in session:
            return redirect("/loginview")

        title = request.form['title']
        price = request.form['price']
        description = request.form['description']
        user_id = session['user_id']

        # Handle image upload
        if 'image' not in request.files:
            return render_template("newlisting.html", error="No image selected")

        file = request.files['image']
        if file.filename == '':
            return render_template("newlisting.html", error="No file selected")

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            # Save the file only if it's below the maximum allowed size
            try:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            except Exception as e:
                return render_template("newlisting.html", error="Error uploading image")

            properties.add_property(
                title, price, description, filename, user_id)

            flash("Property listed successfully!", "success")
            return redirect("/")

        return render_template("newlisting.html", error="Error creating listing")

    @app.route("/bookings")
    def view_bookings():
        """
        Route to display all the bookings made by the logged-in user.
        Redirects to the login page if the user is not logged in.
        """
        if 'user_id' not in session:
            return redirect("/loginview")

        user_id = session['user_id']
        bookings = properties.get_user_bookings(
            user_id)  # Fetch bookings from the database
        return render_template("profileview.html", rented_properties=bookings)

    @app.route("/book_property/<int:property_id>", methods=["POST"])
    def book_property(property_id):
        """
        Route to handle property booking.
        Validates the booking dates and stores the booking in the database.
        If the user is not logged in, they are redirected to the login page.
        """
        if 'user_id' not in session:
            return redirect("/loginview")

        user_id = session['user_id']
        start_date = request.form["start_date"]
        end_date = request.form["end_date"]

        # Validate the dates
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            if start_date >= end_date:
                flash("Invalid date range", "error")
                return redirect(f"/property/{property_id}")
        except ValueError:
            flash("Invalid date format", "error")
            return redirect(f"/property/{property_id}")

        # Use properties.py to book the property
        try:
            properties.book_property(
                user_id, property_id, start_date, end_date)
            flash("Property booked successfully!", "success")
            return redirect("/bookings")
        except Exception as e:
            flash(f"Error booking property: {str(e)}", "error")
            return redirect(f"/property/{property_id}")

    @app.route("/property/<int:property_id>")
    def view_property(property_id):
        """
        Route to display the details of a specific property.
        Fetches the property details from the database and renders the booking view.
        If the property is not found, an error page is displayed.
        """
        property = properties.get_property_by_id(property_id)
        if not property:
            return render_template("error.html", error="Property not found")

        # URL to access the image file from the static folder
        image_url = url_for('static', filename=f'images/{property.image_url}')
        return render_template("bookingview.html", property=property, image_url=image_url)

    @app.route('/delete_booking/<int:booking_id>', methods=['POST'])
    def delete_booking(booking_id):
        """
        Route to handle the deletion of a booking by the logged-in user.
        Calls the `delete_booking` function from `properties.py` to remove the booking from the database.
        If successful, the user is redirected back to their profile view with a success message.
        """
        if 'user_id' not in session:
            return redirect('/loginview')

        user_id = session['user_id']

        result = properties.delete_booking(booking_id, user_id)

        if result:
            flash('Booking deleted successfully!', 'success')
        else:
            flash('Failed to delete booking.', 'error')

        return redirect('/profileview')
