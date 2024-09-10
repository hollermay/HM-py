import sqlite3
from database import create_connection

def make_reservation(guest_id, room_id, check_in_date, check_out_date):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reservations (guest_id, room_id, check_in_date, check_out_date) VALUES (?, ?, ?, ?)", 
                   (guest_id, room_id, check_in_date, check_out_date))
    conn.commit()
    conn.close()

def update_reservation(reservation_id, guest_id, room_id, check_in_date, check_out_date):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE reservations SET guest_id = ?, room_id = ?, check_in_date = ?, check_out_date = ? WHERE id = ?", 
                   (guest_id, room_id, check_in_date, check_out_date, reservation_id))
    conn.commit()
    conn.close()

def cancel_reservation(reservation_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reservations WHERE id = ?", (reservation_id,))
    conn.commit()
    conn.close()

def get_reservation(reservation_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations WHERE id = ?", (reservation_id,))
    reservation = cursor.fetchone()
    conn.close()
    return reservation

def get_all_reservations():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations")
    reservations = cursor.fetchall()
    conn.close()
    return reservations
