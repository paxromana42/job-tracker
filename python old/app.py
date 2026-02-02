import streamlit as st
import sqlite3
from datetime import date
from pathlib import Path

CHECK = "If you can see this, Streamlit is running the script."

st.set_page_config(page_title="J*b Application Tracker", layout="wide")
st.title("J*b Application Tracker")
st.caption(CHECK)

DB_PATH = Path("db/tracker.db")
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

@st.cache_resource
def get_conn():
    # cache_resource keeps one connection per session
    return sqlite3.connect(DB_PATH, check_same_thread=False)

conn = get_conn()

def init_db(c: sqlite3.Connection) -> None:
    c.execute("""
    CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date_applied TEXT NOT NULL,
        date_posted TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'Applied',
        job_title TEXT NOT NULL,
        company TEXT NOT NULL,
        address TEXT,
        source TEXT,
        link TEXT,
        updated TEXT NOT NULL
    );
    """)
    c.execute("CREATE INDEX IF NOT EXISTS idx_app_status ON applications(status);")
    c.execute("CREATE INDEX IF NOT EXISTS idx_app_company ON applications(company);")
    c.commit()

init_db(conn)

st.subheader("Add New Application")

with st.form("add_application", clear_on_submit=True):
    job_title = st.text_input("Job Title", placeholder="e.g., IT Support Engineer I")
    company = st.text_input("Company", placeholder="e.g., Xantrion")
    location = st.text_input("Location", placeholder="e.g., New York, NY")
    source = st.text_input("Source", placeholder="e.g., LinkedIn")
    link = st.text_input("Job Link", placeholder="Paste URL here")

    # Optional fields you had in Excel
    status = st.selectbox("Status", ["Applied", "Interview", "Offer", "Rejected", "Ghosted"], index=0)
    date_applied = st.date_input("Date Applied", value=date.today())
    date_posted = st.date_input("Date Posted", value=date.today())
    updated = st.date_input("Updated", value=date.today())

    submitted = st.form_submit_button("Add")

if submitted:
    # Basic validation
    if not job_title.strip() or not company.strip():
        st.error("Job Title and Company are required.")
    else:
        conn.execute(
            """
            INSERT INTO applications (date_applied, status, job_title, company, location, source, link, updated)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            """,
            (
                date_applied.isoformat(),
                status,
                job_title.strip(),
                company.strip(),
                location.strip() if location else None,
                source.strip() if source else None,
                link.strip() if link else None,
                updated.isoformat(),
            ),
        )
        conn.commit()
        st.success(f"Saved: {job_title} at {company}")

st.divider()
st.subheader("Saved Applications")

# Simple filters
col1, col2 = st.columns(2)
with col1:
    filter_status = st.selectbox("Filter by status", ["(All)", "Applied", "Interview", "Offer", "Rejected", "Ghosted"])
with col2:
    search_company = st.text_input("Search company", placeholder="Type part of a company name")

query = "SELECT id, date_applied, status, job_title, company, location, source, link, updated FROM applications"
params = []
clauses = []

if filter_status != "(All)":
    clauses.append("status = ?")
    params.append(filter_status)

if search_company.strip():
    clauses.append("company LIKE ?")
    params.append(f"%{search_company.strip()}%")

if clauses:
    query += " WHERE " + " AND ".join(clauses)

query += " ORDER BY date_applied DESC, id DESC LIMIT 200;"

rows = conn.execute(query, params).fetchall()

if not rows:
    st.info("No applications yet.")
else:
    # Render as a table without pandas
    st.dataframe(
        rows,
        use_container_width=True,
        column_config={
            0: st.column_config.NumberColumn("ID"),
            1: "Date",
            2: "Status",
            3: "Job Title",
            4: "Company",
            5: "Location",
            6: "Source",
            7: "Link",
            8: "Updated",
        },
    )
