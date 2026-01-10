from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # INSECURE: SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)

    user = cursor.fetchone()
    conn.close()

    if user:
        return "Login Successful"
    else:
        return "Invalid Credentials"

if __name__ == "__main__":
    app.run(debug=True)  # INSECURE
