import sqlite3
import datetime
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
# Connect to the database
conn = sqlite3.connect("events.db")
cursor = conn.cursor()

# Add a test event for the current time
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
cursor.execute("INSERT INTO events (date, time, event) VALUES (?, ?, ?)", (current_time.split()[0], current_time.split()[1], "Test Reminder Now"))
conn.commit()

# Check the events
cursor.execute("SELECT * FROM events")
print(cursor.fetchall())

conn.close()