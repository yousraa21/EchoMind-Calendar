import sqlite3

import sqlite3

def init_db():
    """Reinitialize the database and create the correct table."""
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()

    # Drop the old table (WARNING: This will delete all saved events)
    cursor.execute("DROP TABLE IF EXISTS events")

    # Create the correct table with a 'time' column
    cursor.execute("""
        CREATE TABLE events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            time TEXT,
            event TEXT
        )
    """)

    conn.commit()
    conn.close()

# Run this function once to update your database
if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")

def save_event(date, time, event_text):
    """Save an event to the database with both date and time."""
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO events (date, time, event) VALUES (?, ?, ?)", (date, time, event_text))
    conn.commit()
    conn.close()

def get_events_for_date(date):
    """Retrieve events for a specific date."""
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()
    cursor.execute("SELECT time, event FROM events WHERE date=?", (date,))
    events = cursor.fetchall()
    conn.close()
    return events
