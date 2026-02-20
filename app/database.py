import sqlite3

DB_NAME = "tickets.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            ticket_id TEXT PRIMARY KEY,
            message TEXT NOT NULL,
            category TEXT,
            confidence REAL,
            draft_reply TEXT,
            needs_review INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def insert_ticket(ticket_data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tickets 
        (ticket_id, message, category, confidence, draft_reply, needs_review)
        VALUES (?, ?, ?, ?, ?, ?)
    """, ticket_data)

    conn.commit()
    conn.close()


def ticket_exists(ticket_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM tickets WHERE ticket_id = ?", (ticket_id,))
    result = cursor.fetchone()

    conn.close()
    return result is not None


def get_review_tickets():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tickets WHERE needs_review = 1")
    rows = cursor.fetchall()

    conn.close()
    return rows
