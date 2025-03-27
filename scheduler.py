from PyQt6.QtCore import QTimer, QObject, pyqtSignal
import sqlite3
import datetime

class Scheduler(QObject):
    # Define a signal to trigger reminders
    reminder_triggered = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.timeout.connect(self.check)
        self.timer.start(60000)  # Check every minute
        print("Scheduler started.")  # Debug

    def check_reminders(self):
        """Check the database for upcoming reminders."""
        conn = sqlite3.connect("events.db")
        cursor = conn.cursor()

        # Get the current date and time in the correct format
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        print(f"Current time: {now}")  # Debug

        # Query for reminders
        query = "SELECT date, time, event FROM events WHERE date || ' ' || time = ?"
        print(f"Executing query: {query} with now = {now}")  # Debug
        cursor.execute(query, (now,))
        reminders = cursor.fetchall()
        conn.close()
        return reminders

    def check(self):
        """Periodically check for reminders and emit signals."""
        print("Checking for reminders...")  # Debug
        reminders = self.check_reminders()
        print(f"Reminders found: {reminders}")  # Debug
        for date, event_time, event in reminders:
            print(f"Triggering reminder: {event}")  # Debug
            self.reminder_triggered.emit(event)  # Emit the signal