import csv
import datetime
import sqlite3
from pathlib import Path

# Database logic (CRUD)

# ====== Create =========

# Create the database
def create_database_file(accepted_path):
    accepted_path = str(accepted_path)

    # Ensure parent folder exists
    Path(accepted_path).parent.mkdir(parents=True, exist_ok=True)

    print(f"Creating database at: {accepted_path}")

    try:
        conn = sqlite3.connect(accepted_path)
        cursor = conn.cursor()

        # Enable foreign keys
        cursor.execute("PRAGMA foreign_keys = ON;")

        # ---------------------------
        # APPLICATIONS TABLE (UPDATED)
        # ---------------------------
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            created_at TEXT NOT NULL,
            posted_at TEXT,

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

        # ---------------------------
        # UPDATES TABLE
        # ---------------------------
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

        conn.commit()
        print("Database schema created successfully.")
    except sqlite3.Error as e:
        print(f"Failed to create database schema: {e}")
    finally:
        conn.close()
        print("Database connection closed.")

# Insert applications (individual)
def add_application(
    db_path,
    title,
    company,
    posted_at=None,
    location=None,
    source=None,
    link=None,
    wage_min=None,
    wage_max=None,
    pay_frequency=None,
    hours_per_week=None
):

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO applications (
        created_at,
        posted_at,
        title,
        company,
        location,
        source,
        link,
        wage_range_min,
        wage_range_max,
        pay_frequency,
        hours_per_week
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().isoformat(),
        posted_at,
        title,
        company,
        location,
        source,
        link,
        wage_min,
        wage_max,
        pay_frequency,
        hours_per_week
    ))

    conn.commit()
    conn.close()

# Import CSVs (mass input)
def bulk_insert_from_csv(db_path, file_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        rows = []
        for row in reader:
            rows.append((
                row.get("created_at"),
                row.get("posted_at"),
                row.get("title"),
                row.get("company"),
                row.get("location"),
                row.get("source"),
                row.get("link"),
                row.get("wage_range_min"),
                row.get("wage_range_max"),
                row.get("pay_frequency"),
                row.get("hours_per_week"),
            ))

        cur.executemany("""
        INSERT INTO applications (
            created_at, posted_at, title, company, location, source, link,
            wage_range_min, wage_range_max, pay_frequency, hours_per_week
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, rows)

    conn.commit()
    conn.close()

    print(f"{len(rows)} records inserted.")

# ====== Read =========
def get_all_applications(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, title, company, location,
                wage_range_min, wage_range_max,
                pay_frequency, created_at
        FROM applications
        ORDER BY created_at DESC
    """)
    return cursor.fetchall()

def view_updates(db_path, application_id):
    conn = sqlite3.connect(db_path)

    for row in conn.execute("""
        SELECT timestamp, status, note
        FROM application_updates
        WHERE application_id = ?
        ORDER BY timestamp DESC
    """, (application_id,)):
        print(row)

    conn.close()

# ====== Update =========
def insert_update(db_path, app_id, timestamp, status, note):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO application_updates (application_id, timestamp, status, note)
        VALUES (?, ?, ?, ?)
    """, (app_id, timestamp, status, note))

    conn.commit()
    conn.close()


# ====== Delete =========
def delete_application(conn, app_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM applications WHERE id = ?", (app_id,))
    conn.commit()

