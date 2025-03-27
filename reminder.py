from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication, QSizePolicy
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QTimer
import pyttsx3
import threading

class ReminderPopup(QWidget):
    """Popup window that appears when an event reminder is triggered."""
    def __init__(self, logo_path, text):
        super().__init__()
        self.setWindowTitle("EchoMind - Reminder")
        self.setFixedSize(400, 300)  # Increased width to accommodate longer text
        self.setStyleSheet("background-color: #fce4ec; border-radius: 15px;")

        layout = QVBoxLayout(self)

        # Logo
        self.logo_label = QLabel(self)
        pixmap = QPixmap(logo_path)
        self.logo_label.setPixmap(pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio))
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Text
        self.text_label = QLabel(text)
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_label.setWordWrap(True)  # Enable word wrapping
        self.text_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)  # Allow the label to expand

        layout.addWidget(self.logo_label)
        layout.addWidget(self.text_label)

        self.setLayout(layout)

        # Debug: Confirm the popup is being created
        print("ReminderPopup created with text:", text)

        # Play reminder voice
        self.play_voice(text)

        # Auto-close the popup after 10 seconds
        self.timer = QTimer()
        self.timer.timeout.connect(self.close)
        self.timer.start(10000)  # 10,000 ms = 10 seconds
        print("Auto-close timer started.")  # Debug

    def play_voice(self, text):
        """Play the reminder using text-to-speech."""
        def voice_thread():
            try:
                engine = pyttsx3.init()
                engine.say(text)
                engine.runAndWait()
            except Exception as e:
                print(f"Error during voice playback: {e}")

        # Start the voice playback in a separate thread
        threading.Thread(target=voice_thread, daemon=True).start()

    def show(self):
        """Override the show method to ensure the window is visible."""
        super().show()
        QApplication.processEvents()  # Force the event loop to update
        print("ReminderPopup shown.")  # Debug

    def closeEvent(self, event):
        """Override the close event to clean up resources."""
        print("ReminderPopup closed.")  # Debug
        self.timer.stop()  # Stop the timer when the window is closed
        super().closeEvent(event)