import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from auth import register_user, login_user
from guest import add_guest, get_all_guests
from room import add_room, get_all_rooms
from reservation import make_reservation, get_all_reservations
from billing import add_bill, get_all_bills
from database import setup_database

class HotelManagementSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        setup_database()

    def initUI(self):
        self.setWindowTitle('Hotel Management System')
        self.setGeometry(100, 100, 800, 600)

        self.main_layout = QVBoxLayout()

        self.username_label = QLabel('Username:')
        self.username_input = QLineEdit()
        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.login)

        self.main_layout.addWidget(self.username_label)
        self.main_layout.addWidget(self.username_input)
        self.main_layout.addWidget(self.password_label)
        self.main_layout.addWidget(self.password_input)
        self.main_layout.addWidget(self.login_button)

        container = QWidget()
        container.setLayout(self.main_layout)
        self.setCentralWidget(container)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        user = login_user(username, password)
        if user:
            QMessageBox.information(self, 'Login Successful', 'Welcome!')
            self.show_main_menu()
        else:
            QMessageBox.warning(self, 'Login Failed', 'Invalid credentials. Please try again.')

    def show_main_menu(self):
        self.clear_layout(self.main_layout)

        self.add_guest_button = QPushButton('Add Guest')
        self.add_guest_button.clicked.connect(self.add_guest)
        self.view_guests_button = QPushButton('View Guests')
        self.view_guests_button.clicked.connect(self.view_guests)
        self.add_room_button = QPushButton('Add Room')
        self.add_room_button.clicked.connect(self.add_room)
        self.view_rooms_button = QPushButton('View Rooms')
        self.view_rooms_button.clicked.connect(self.view_rooms)
        self.make_reservation_button = QPushButton('Make Reservation')
        self.make_reservation_button.clicked.connect(self.make_reservation)
        self.view_reservations_button = QPushButton('View Reservations')
        self.view_reservations_button.clicked.connect(self.view_reservations)
        self.add_bill_button = QPushButton('Add Bill')
        self.add_bill_button.clicked.connect(self.add_bill)
        self.view_bills_button = QPushButton('View Bills')
        self.view_bills_button.clicked.connect(self.view_bills)

        self.main_layout.addWidget(self.add_guest_button)
        self.main_layout.addWidget(self.view_guests_button)
        self.main_layout.addWidget(self.add_room_button)
        self.main_layout.addWidget(self.view_rooms_button)
        self.main_layout.addWidget(self.make_reservation_button)
        self.main_layout.addWidget(self.view_reservations_button)
        self.main_layout.addWidget(self.add_bill_button)
        self.main_layout.addWidget(self.view_bills_button)

    def add_guest(self):
        self.clear_layout(self.main_layout)

        self.name_label = QLabel('Name:')
        self.name_input = QLineEdit()
        self.phone_label = QLabel('Phone:')
        self.phone_input = QLineEdit()
        self.email_label = QLabel('Email:')
        self.email_input = QLineEdit()
        self.add_guest_submit_button = QPushButton('Submit')
        self.add_guest_submit_button.clicked.connect(self.add_guest_to_db)

        self.main_layout.addWidget(self.name_label)
        self.main_layout.addWidget(self.name_input)
        self.main_layout.addWidget(self.phone_label)
        self.main_layout.addWidget(self.phone_input)
        self.main_layout.addWidget(self.email_label)
        self.main_layout.addWidget(self.email_input)
        self.main_layout.addWidget(self.add_guest_submit_button)

    def add_guest_to_db(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()

        add_guest(name, phone, email)
        QMessageBox.information(self, 'Guest Added', 'Guest has been added successfully.')
        self.show_main_menu()

    def view_guests(self):
        self.clear_layout(self.main_layout)
        guests = get_all_guests()

        for guest in guests:
            guest_info = QLabel(f"ID: {guest[0]}, Name: {guest[1]}, Phone: {guest[2]}, Email: {guest[3]}")
            self.main_layout.addWidget(guest_info)

        self.back_button = QPushButton('Back')
        self.back_button.clicked.connect(self.show_main_menu)
        self.main_layout.addWidget(self.back_button)

    def add_room(self):
        self.clear_layout(self.main_layout)

        self.room_number_label = QLabel('Room Number:')
        self.room_number_input = QLineEdit()
        self.room_type_label = QLabel('Room Type:')
        self.room_type_input = QLineEdit()
        self.room_status_label = QLabel('Status:')
        self.room_status_input = QLineEdit()
        self.add_room_submit_button = QPushButton('Submit')
        self.add_room_submit_button.clicked.connect(self.add_room_to_db)

        self.main_layout.addWidget(self.room_number_label)
        self.main_layout.addWidget(self.room_number_input)
        self.main_layout.addWidget(self.room_type_label)
        self.main_layout.addWidget(self.room_type_input)
        self.main_layout.addWidget(self.room_status_label)
        self.main_layout.addWidget(self.room_status_input)
        self.main_layout.addWidget(self.add_room_submit_button)

    def add_room_to_db(self):
        room_number = self.room_number_input.text()
        room_type = self.room_type_input.text()
        status = self.room_status_input.text()

        add_room(room_number, room_type, status)
        QMessageBox.information(self, 'Room Added', 'Room has been added successfully.')
        self.show_main_menu()

    def view_rooms(self):
        self.clear_layout(self.main_layout)
        rooms = get_all_rooms()

        for room in rooms:
            room_info = QLabel(f"ID: {room[0]}, Room Number: {room[1]}, Type: {room[2]}, Status: {room[3]}")
            self.main_layout.addWidget(room_info)

        self.back_button = QPushButton('Back')
        self.back_button.clicked.connect(self.show_main_menu)
        self.main_layout.addWidget(self.back_button)

    def make_reservation(self):
        self.clear_layout(self.main_layout)

        self.guest_id_label = QLabel('Guest ID:')
        self.guest_id_input = QLineEdit()
        self.room_id_label = QLabel('Room ID:')
        self.room_id_input = QLineEdit()
        self.check_in_date_label = QLabel('Check-In Date:')
        self.check_in_date_input = QLineEdit()
        self.check_out_date_label = QLabel('Check-Out Date:')
        self.check_out_date_input = QLineEdit()
        self.make_reservation_submit_button = QPushButton('Submit')
        self.make_reservation_submit_button.clicked.connect(self.add_reservation_to_db)

        self.main_layout.addWidget(self.guest_id_label)
        self.main_layout.addWidget(self.guest_id_input)
        self.main_layout.addWidget(self.room_id_label)
        self.main_layout.addWidget(self.room_id_input)
        self.main_layout.addWidget(self.check_in_date_label)
        self.main_layout.addWidget(self.check_in_date_input)
        self.main_layout.addWidget(self.check_out_date_label)
        self.main_layout.addWidget(self.check_out_date_input)
        self.main_layout.addWidget(self.make_reservation_submit_button)

    def add_reservation_to_db(self):
        guest_id = self.guest_id_input.text()
        room_id = self.room_id_input.text()
        check_in_date = self.check_in_date_input.text()
        check_out_date = self.check_out_date_input.text()

        make_reservation(guest_id, room_id, check_in_date, check_out_date)
        QMessageBox.information(self, 'Reservation Made', 'Reservation has been made successfully.')
        self.show_main_menu()

    def view_reservations(self):
        self.clear_layout(self.main_layout)
        reservations = get_all_reservations()

        for reservation in reservations:
            reservation_info = QLabel(f"ID: {reservation[0]}, Guest ID: {reservation[1]}, Room ID: {reservation[2]}, Check-In: {reservation[3]}, Check-Out: {reservation[4]}")
            self.main_layout.addWidget(reservation_info)

        self.back_button = QPushButton('Back')
        self.back_button.clicked.connect(self.show_main_menu)
        self.main_layout.addWidget(self.back_button)

    def add_bill(self):
        self.clear_layout(self.main_layout)

        self.reservation_id_label = QLabel('Reservation ID:')
        self.reservation_id_input = QLineEdit()
        self.amount_label = QLabel('Amount:')
        self.amount_input = QLineEdit()
        self.add_bill_submit_button = QPushButton('Submit')
        self.add_bill_submit_button.clicked.connect(self.add_bill_to_db)

        self.main_layout.addWidget(self.reservation_id_label)
        self.main_layout.addWidget(self.reservation_id_input)
        self.main_layout.addWidget(self.amount_label)
        self.main_layout.addWidget(self.amount_input)
        self.main_layout.addWidget(self.add_bill_submit_button)

    def add_bill_to_db(self):
        reservation_id = self.reservation_id_input.text()
        amount = self.amount_input.text()

        add_bill(reservation_id, amount)
        QMessageBox.information(self, 'Bill Added', 'Bill has been added successfully.')
        self.show_main_menu()

    def view_bills(self):
        self.clear_layout(self.main_layout)
        bills = get_all_bills()

        for bill in bills:
            bill_info = QLabel(f"ID: {bill[0]}, Reservation ID: {bill[1]}, Amount: {bill[2]}")
            self.main_layout.addWidget(bill_info)

        self.back_button = QPushButton('Back')
        self.back_button.clicked.connect(self.show_main_menu)
        self.main_layout.addWidget(self.back_button)

    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HotelManagementSystem()
    window.show()
    sys.exit(app.exec_())
