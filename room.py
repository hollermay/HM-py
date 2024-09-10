import sqlite3
from database import create_connection

def add_room(room_number, room_type, status):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO rooms (room_number, room_type, status) VALUES (?, ?, ?)", (room_number, room_type, status))
    conn.commit()
    conn.close()

def update_room(room_id, room_number, room_type, status):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE rooms SET room_number = ?, room_type = ?, status = ? WHERE id = ?", (room_number, room_type, status, room_id))
    conn.commit()
    conn.close()

def delete_room(room_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM rooms WHERE id = ?", (room_id,))
    conn.commit()
    conn.close()

def get_room(room_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rooms WHERE id = ?", (room_id,))
    room = cursor.fetchone()
    conn.close()
    return room

def get_all_rooms():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rooms")
    rooms = cursor.fetchall()
    conn.close()
    return rooms
