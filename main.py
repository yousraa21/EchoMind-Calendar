import sys
from PyQt6.QtWidgets import QApplication
from gui import CalendarWindow
from database import init_db
from scheduler import Scheduler
from reminder import ReminderPopup
from gui import load_stylesheet

class MainApp:
    def __init__(self):
        # Initialize the database
        init_db()

        # Start QApplication
        self.app = QApplication(sys.argv)
        self.app.setStyleSheet(load_stylesheet())  # Apply the pastel theme

        # Start the scheduler
        self.scheduler = Scheduler()
        self.scheduler.reminder_triggered.connect(self.show_reminder)  # Connect signal to slot

        # Start the main GUI
        self.main_window = CalendarWindow()
        self.main_window.show()

        # Store a reference to the ReminderPopup
        self.reminder_popup = None

        sys.exit(self.app.exec())

    def show_reminder(self, text):
        """Slot to show the reminder popup."""
        print(f"Showing reminder: {text}")  # Debug
        self.reminder_popup = ReminderPopup("assets/echomind_logo.png", text)
        self.reminder_popup.show()
        print("ReminderPopup should be visible now.")  # Debug

if __name__ == "__main__":
    MainApp()