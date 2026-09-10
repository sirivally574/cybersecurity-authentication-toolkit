from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import re
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key is used to protect user sessions
app.secret_key = "change-this-secret-key"

DATABASE = "users.db"


# ---------------- DATABASE ----------------

def get_db():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def create_database():
    connection = get_db()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


# ---------------- PASSWORD CHECK ----------------

def check_password_strength(password):

    if len(password) < 8:
        return False, "Password must contain at least 8 characters."

    if not re.search(r"[A-Z]", password):
        return False, "Password must contain an uppercase letter."

    if not re.search(r"[a-z]", password):
        return False, "Password must contain a lowercase letter."

    if not re.search(r"[0-9]", password):
        return False, "Password must contain a number."

    if not re.search(r"[^A-Za-z0-9]", password):
        return False, "Password must contain a special character."

    return True, "Strong password."


# ---------------- HOME ----------------

@app.route("/")
def home():

    if "user_id" in session:
        return redirect(url_for("dashboard"))

    return redirect(url_for("login"))


# ---------------- REGISTER ----------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"].strip()
        email = request.form["email"].strip()
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        # Check empty fields
        if not username or not email or not password:
            flash("All fields are required.")
            return redirect(url_for("register"))

        # Check email format
        if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
            flash("Enter a valid email address.")
            return redirect(url_for("register"))

        # Check password confirmation
        if password != confirm_password:
            flash("Passwords do not match.")
            return redirect(url_for("register"))

        # Check password strength
        strong, message = check_password_strength(password)

        if not strong:
            flash(message)
            return redirect(url_for("register"))

        connection = get_db()

        # Check if email already exists
        existing_user = connection.execute(
            "SELECT id FROM users WHERE email = ?",
            (email,)
        ).fetchone()

        if existing_user:
            connection.close()
            flash("An account with this email already exists.")
            return redirect(url_for("register"))

        # HASH PASSWORD
        password_hash = generate_password_hash(password)

        # Store user
        connection.execute(
            """
            INSERT INTO users (username, email, password_hash)
            VALUES (?, ?, ?)
            """,
            (username, email, password_hash)
        )

        connection.commit()
        connection.close()

        flash("Registration successful. Please login.")
        return redirect(url_for("login"))

    return render_template("register.html")


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"].strip()
        password = request.form["password"]

        connection = get_db()

        user = connection.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        ).fetchone()

        connection.close()

        # Check password
        if user and check_password_hash(user["password_hash"], password):

            # Create session
            session["user_id"] = user["id"]
            session["username"] = user["username"]

            flash("Login successful!")

            return redirect(url_for("dashboard"))

        flash("Invalid email or password.")

    return render_template("login.html")


# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():

    # Only logged-in users can access dashboard
    if "user_id" not in session:
        flash("Please login first.")
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        username=session["username"]
    )


# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():

    session.clear()

    flash("You have been logged out.")

    return redirect(url_for("login"))


# ---------------- START APPLICATION ----------------
if __name__ == "__main__":
    create_database()
    app.run(host="0.0.0.0", port=5000)