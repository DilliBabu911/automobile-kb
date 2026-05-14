import sqlite3

DB_FILE = "complaints.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            complaint TEXT NOT NULL,
            answer TEXT NOT NULL,
            asked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_complaint(complaint: str, answer: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO complaints (complaint, answer) VALUES (?, ?)",
        (complaint, answer)
    )
    conn.commit()
    conn.close()

def get_all_complaints():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, complaint, answer, asked_at FROM complaints ORDER BY asked_at DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_complaint(complaint_id: int):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM complaints WHERE id = ?", (complaint_id,))
    conn.commit()
    conn.close()
