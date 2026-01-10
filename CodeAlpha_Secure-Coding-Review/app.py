from flask import Flask, request
import sqlite3
from werkzeug.security import check_password_hash

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return "Missing credentials", 400

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password FROM users WHERE username = ?",
        (username,)
    )

    user = cursor.fetchone()
    conn.close()

    if user and check_password_hash(user[0], password):
        return "Login Successful"
    else:
        return "Invalid Credentials", 401

if __name__ == "__main__":
    app.run(debug=False)
