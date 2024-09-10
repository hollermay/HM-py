import sqlite3
from database import create_connection

def add_bill(reservation_id, amount):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO billing (reservation_id, amount) VALUES (?, ?)", (reservation_id, amount))
    conn.commit()
    conn.close()

def get_bill(bill_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM billing WHERE id = ?", (bill_id,))
    bill = cursor.fetchone()
    conn.close()
    return bill

def get_all_bills():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM billing")
    bills = cursor.fetchall()
    conn.close()
    return bills
