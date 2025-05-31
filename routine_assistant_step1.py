from datetime import datetime
import time
import pyttsx3
import sqlite3

robot = pyttsx3.init()

# Connect to the DB
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Get all reminders for all users (or filter by user if needed)
cursor.execute("SELECT time, task FROM routine")
rows = cursor.fetchall()

# Build the routine dictionary
routine = {time: task for time, task in rows}

print("Assistant is running...")

while True:
    now = datetime.now().strftime("%H:%M")
    if now in routine:
        task = routine[now]
        print(f"🔔 It's {now}. Time for: {task}")
        robot.say(f"It's {now}. Time for {task}")
        robot.runAndWait()
        time.sleep(60)
    else:
        print(f"⏰ {now} - No reminder")
        time.sleep(60)
