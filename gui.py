from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QCalendarWidget, QLabel, QTextEdit, QTimeEdit
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QPixmap
from database import save_event, get_events_for_date
from reminder import ReminderPopup
import sys

def load_stylesheet():
    with open("theme.qss", "r") as file:
        return file.read()
class CalendarWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EchoMind - Calendar")
        self.setGeometry(100, 100, 360, 600)
        layout = QVBoxLayout()

        # Logo
        self.logo_label = QLabel(self)
        pixmap = QPixmap("assets/echomind_logo.png")
        self.logo_label.setPixmap(pixmap.scaled(150, 100))
        layout.addWidget(self.logo_label)

        # Calendar
        self.calendar = QCalendarWidget(self)
        self.calendar.clicked.connect(self.open_event_window)
        layout.addWidget(self.calendar)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_event_window(self, date: QDate):
        self.event_window = EventWindow(date)
        self.event_window.show()

class EventWindow(QWidget):
    def __init__(self, date):
        super().__init__()
        self.setWindowTitle("Add Event")
        self.setGeometry(150, 150, 300, 200)
        self.date = date.toString("yyyy-MM-dd")
        
        layout = QVBoxLayout()
        self.label = QLabel(f"Add event for {self.date}:")
        self.text_edit = QTextEdit()
        self.time_edit = QTimeEdit()  # New time picker
        self.add_button = QPushButton("Add Event")
        self.add_button.clicked.connect(self.save_event)
        
        layout.addWidget(self.label)
        layout.addWidget(self.time_edit)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.add_button)
        
        self.setLayout(layout)
    
    def save_event(self):
        event_text = self.text_edit.toPlainText()
        event_time = self.time_edit.time().toString("HH:mm")  # Get time in 24-hour format
        if event_text:
            save_event(self.date, event_time, event_text)
            self.close()

# Run the GUI
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(load_stylesheet())  # Apply the pastel theme
    main_window = CalendarWindow()
    main_window.show()
    sys.exit(app.exec())
