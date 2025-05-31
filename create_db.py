import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

# Drop tables if they exist (optional, to avoid duplication errors)
c.execute('DROP TABLE IF EXISTS users')
c.execute('DROP TABLE IF EXISTS reminders')
c.execute('DROP TABLE IF EXISTS routine')

# Create users table
c.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Create reminders table with 'message' column
c.execute('''
CREATE TABLE reminders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    message TEXT,
    time TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
''')

# Create routine table
c.execute('''
CREATE TABLE routine (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    time TEXT,
    task TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
''')

conn.commit()
conn.close()
print("Database created successfully.")
