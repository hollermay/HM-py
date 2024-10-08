import sqlite3
from database import create_connection

def register_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def login_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

predefined_username = "admin"
predefined_password = "password123"

# Register the predefined user (you can do this once during setup)
register_user(predefined_username, predefined_password)

# Example usage
if login_user("admin", "password123"):
    print("Login successful!")
else:
    print("Login failed.")