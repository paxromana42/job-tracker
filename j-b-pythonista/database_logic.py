import sqlite3

def create_database_file(accepted_path=None):
    print("Creating database file...")
    # Code to create the database file goes here
    connection = sqlite3.connect(accepted_path)  # Creates jobs.db in your project folder
    cursor = connection.cursor()

    # Create applications table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TEXT NOT NULL,
        title TEXT NOT NULL,
        company TEXT NOT NULL,
        location TEXT,
        source TEXT,
        link TEXT
    );
    """)

    # Create application_updates table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS application_updates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        application_id INTEGER NOT NULL,
        timestamp TEXT NOT NULL,
        status TEXT NOT NULL,
        note TEXT,
        FOREIGN KEY(application_id) REFERENCES applications(id)
    );
    """)

    connection.commit()  # Save changes
    connection.close()   # Close connection
