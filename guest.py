import sqlite3
from database import create_connection

def add_guest(name, phone, email):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO guests (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    conn.close()

def update_guest(guest_id, name, phone, email):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE guests SET name = ?, phone = ?, email = ? WHERE id = ?", (name, phone, email, guest_id))
    conn.commit()
    conn.close()

def delete_guest(guest_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM guests WHERE id = ?", (guest_id,))
    conn.commit()
    conn.close()

def get_guest(guest_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM guests WHERE id = ?", (guest_id,))
    guest = cursor.fetchone()
    conn.close()
    return guest

def get_all_guests():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM guests")
    guests = cursor.fetchall()
    conn.close()
    return guests
