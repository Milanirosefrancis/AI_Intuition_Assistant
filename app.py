from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from datetime import datetime
import pyttsx3

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def speak_reminders():
    engine = pyttsx3.init()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    now = datetime.now().strftime("%I:%M %p")  # 12-hour format
    c.execute("SELECT message FROM reminders WHERE time = ? AND done = 0", (now,))
    reminders = c.fetchall()
    for reminder in reminders:
        engine.say(reminder[0])
    engine.runAndWait()
    conn.close()

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        username = request.form['username']
        password = request.form['password']
        c.execute("SELECT id FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            session['user_id'] = user[0]
            return redirect(url_for('home'))
        else:
            flash("Invalid credentials")
            return render_template('login.html')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        username = request.form['username']
        password = request.form['password']
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
        except sqlite3.IntegrityError:
            flash("Username already taken")
            return render_template('register.html')
        conn.close()
        flash("Registration successful! Please login.")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT id, message, time, done FROM reminders WHERE user_id = ?", (user_id,))
    reminders = c.fetchall()
    conn.close()
    speak_reminders()
    return render_template('home.html', reminders=reminders)

@app.route('/add_reminder', methods=['POST'])
def add_reminder():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    message = request.form['message']
    time = request.form['time']
    user_id = session['user_id']
    conn = sqlite3.connect('users.db')
    conn.execute("INSERT INTO reminders (user_id, message, time, done) VALUES (?, ?, ?, 0)", (user_id, message, time))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/mark_done/<int:reminder_id>')
def mark_done(reminder_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    conn = sqlite3.connect('users.db')
    conn.execute("UPDATE reminders SET done = 1 WHERE id = ?", (reminder_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
