import sqlite3
from datetime import datetime

class DBProxy:
    def __init__(self, db_name="scores.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS scores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    score INTEGER NOT NULL,
                    date TEXT NOT NULL,
                    time TEXT NOT NULL
                )
            """)

    def add_score(self, name, score):
        date_str = datetime.now().strftime("%Y-%m-%d")
        time_str = datetime.now().strftime("%H:%M:%S")
        with self.conn:
            self.conn.execute("""
                INSERT INTO scores (name, score, date, time)
                VALUES (?, ?, ?, ?)
            """, (name, score, date_str, time_str))

    def get_top_scores(self, limit=10):
        with self.conn:
            return list(self.conn.execute("""
                SELECT name, score, date, time FROM scores ORDER BY score DESC LIMIT ?
            """, (limit,)))