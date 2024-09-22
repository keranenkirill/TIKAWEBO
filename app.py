from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash
from os import getenv

app = Flask(__name__)
# koodi määrittelee osoitteen, jonka kautta tietokantaan saadaan yhteys
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
# sekä luo db-olion, jonka avulla sovellus voi suorittaa SQL-komentoja.
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/loginview")
def login():
    return render_template("loginview.html")


@app.route("/registerview")
def registerview():
    return render_template("registerview.html")


@app.route("/createuser", methods=["POST"])
def createuser():
    username = request.form["username"]
    psswd1 = request.form["password1"]
    psswd2 = request.form["password2"]

    if not username or not psswd1 or not psswd2:
        return render_template("registerview.html", error="Please fill all fields")
    if psswd1 != psswd2:
        return render_template("registerview.html", error="Passwords do not match")

    # Check if the username already exists
    sql = text("SELECT id FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username": username})
    if result.fetchone():
        return render_template("registerview.html", error="Username already exists")

    # If everything is fine, create the user
    hash_value = generate_password_hash(psswd1)
    sql = text(
        "INSERT INTO users (username, password) VALUES (:username, :password)")
    db.session.execute(sql, {"username": username, "password": hash_value})
    db.session.commit()

    return render_template("index.html", goodmsg="Username succesfully created")
