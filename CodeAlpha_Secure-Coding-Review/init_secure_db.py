import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# Insert a test user
hashed_password = generate_password_hash("testpass")

cursor.execute(
    "INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)",
    ("testuser", hashed_password)
)

conn.commit()
conn.close()

print("Database initialized successfully")
