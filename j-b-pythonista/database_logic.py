import sqlite3
import TUI as tui

def create_database_file(accepted_path):
    connection = sqlite3.connect(accepted_path)
    cursor = connection.cursor()

    # Enable foreign key enforcement
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Create applications table with pay fields
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TEXT NOT NULL,
        title TEXT NOT NULL,
        company TEXT NOT NULL,
        location TEXT,
        source TEXT,
        link TEXT,
        wage_range_min REAL,
        wage_range_max REAL,
        pay_frequency TEXT,
        hours_per_week INTEGER
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

    connection.commit()
    connection.close()

    print("Database created successfully at" + accepted_path)
