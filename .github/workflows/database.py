import sqlite3
import json

class Database:
    def __init__(self, path='users.db'):
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.create_table()

    def create_table(self):
        cur = self.conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            balance REAL DEFAULT 0,
            discount INTEGER DEFAULT 0,
            crypto_stats TEXT DEFAULT '{}'
        )""")
        self.conn.commit()

    def add_user(self, user_id, username):
        cur = self.conn.cursor()
        cur.execute("INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)", (user_id, username))
        cur.execute("UPDATE users SET username = ? WHERE user_id = ?", (username or '', user_id))
        self.conn.commit()

    def get_user(self, user_id):
        cur = self.conn.cursor()
        cur.execute("SELECT user_id, username, balance, discount, crypto_stats FROM users WHERE user_id = ?", (user_id,))
        row = cur.fetchone()
        if not row:
            return None
        return {'user_id': row[0], 'username': row[1], 'balance': row[2], 'discount': row[3], 'crypto_stats': json.loads(row[4] or '{}')}

    def set_balance(self, user_id, balance):
        cur = self.conn.cursor()
        cur.execute("UPDATE users SET balance = ? WHERE user_id = ?", (balance, user_id))
        self.conn.commit()

    def set_discount(self, user_id, discount):
        cur = self.conn.cursor()
        cur.execute("UPDATE users SET discount = ? WHERE user_id = ?", (discount, user_id))
        self.conn.commit()
