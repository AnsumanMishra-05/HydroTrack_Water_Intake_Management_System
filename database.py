import sqlite3

# ✅ Connect to SQLite DB
def connect_db():
    conn = sqlite3.connect("users.db", check_same_thread=False)
    c = conn.cursor()
    return conn, c

# ✅ Create necessary tables
def create_tables():
    conn, c = connect_db()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS profiles (
                    username TEXT PRIMARY KEY,
                    age INTEGER,
                    weight REAL,
                    gender TEXT,
                    goal REAL)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS water_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    amount INTEGER,
                    date TEXT)''')
    
    conn.commit()
    conn.close()

# ✅ Insert new user
def add_user(username, password):
    conn, c = connect_db()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

# ✅ Get user by username
def get_user(username):
    conn, c = connect_db()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()
    return user

# ✅ Save or update profile
def save_profile(username, age, weight, gender, goal):
    conn, c = connect_db()
    c.execute("REPLACE INTO profiles (username, age, weight, gender, goal) VALUES (?, ?, ?, ?, ?)",
              (username, age, weight, gender, goal))
    conn.commit()
    conn.close()

# ✅ Get profile
def get_profile(username):
    conn, c = connect_db()
    c.execute("SELECT age, weight, gender, goal FROM profiles WHERE username = ?", (username,))
    profile = c.fetchone()
    conn.close()
    return profile

# ✅ Insert water log (used in logger.py)
def insert_water_log(username, amount, date):
    conn, c = connect_db()
    c.execute("INSERT INTO water_logs (username, amount, date) VALUES (?, ?, ?)", (username, amount, date))
    conn.commit()
    conn.close()

# ✅ Get water logs (used in analysis)
def get_water_logs(username):
    conn, c = connect_db()
    c.execute("SELECT amount, date FROM water_logs WHERE username = ? ORDER BY date DESC", (username,))
    logs = c.fetchall()
    conn.close()
    return logs