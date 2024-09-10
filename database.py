import sqlite3

def create_connection():
    conn = sqlite3.connect('hotel_management.db')
    return conn

def setup_database():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS guests (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        phone TEXT NOT NULL,
                        email TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS rooms (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        room_number INTEGER NOT NULL,
                        room_type TEXT NOT NULL,
                        status TEXT NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS reservations (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        guest_id INTEGER,
                        room_id INTEGER,
                        check_in_date TEXT,
                        check_out_date TEXT,
                        FOREIGN KEY(guest_id) REFERENCES guests(id),
                        FOREIGN KEY(room_id) REFERENCES rooms(id))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS billing (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        reservation_id INTEGER,
                        amount REAL,
                        FOREIGN KEY(reservation_id) REFERENCES reservations(id))''')
    conn.commit()
    conn.close()
