import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

try:
    c.execute("ALTER TABLE reminders ADD COLUMN done INTEGER DEFAULT 0")
    print("✅ 'done' column added successfully.")
except sqlite3.OperationalError as e:
    print("⚠️ Column already exists or error occurred:", e)

conn.commit()
conn.close()
