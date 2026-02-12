import sqlite3

import sqlite3

def create_database_file(accepted_path=None):
    if not accepted_path:
        print("Error: No path provided for database creation.")
        return

    print(f"Creating or opening database at: {accepted_path}")

    try:
        connection = sqlite3.connect(accepted_path)
        cursor = connection.cursor()

        # Enable foreign key constraints
        cursor.execute("PRAGMA foreign_keys = ON;")

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

        connection.commit()
        print("Database schema created successfully.")

    except sqlite3.Error as error:
        print(f"Failed to create database: {error}")

    finally:
        if connection:
            connection.close()
            print("Database connection closed.")

