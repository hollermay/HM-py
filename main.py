import sys
from PyQt5.QtWidgets import QApplication
from gui import HotelManagementSystem
from database import setup_database

if __name__ == '__main__':
    # Set up the database
    setup_database()

    # Create the PyQt application
    app = QApplication(sys.argv)

    # Create and show the main window
    window = HotelManagementSystem()
    window.show()

    # Execute the application's main loop
    sys.exit(app.exec_())
