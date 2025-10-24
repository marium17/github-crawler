import sqlite3
from contextlib import contextmanager

DB_NAME = "repos.db"

@contextmanager
def get_conn():
    conn = sqlite3.connect(DB_NAME)
    yield conn
    conn.close()

def setup_schema():
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS repositories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                stars INTEGER,
                fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

def insert_repo(name, stars):
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT OR REPLACE INTO repositories (name, stars)
            VALUES (?, ?)
        """, (name, stars))
        conn.commit()

def export_to_csv(filename="repos.csv"):
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("SELECT name, stars FROM repositories")
        rows = cur.fetchall()

    import csv
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "stars"])
        writer.writerows(rows)



