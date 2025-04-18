import hashlib
import sqlite3
import streamlit as st
from database import connect_db  # Correctly imported function

# Function to hash the password securely using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to register a new user into the database
def register_user(username, password):
    conn, cursor = connect_db()  # Use the correct connection function
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                       (username, hash_password(password)))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

# Function to validate login credentials
def login_user(username, password):
    conn, cursor = connect_db()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", 
                   (username, hash_password(password)))
    result = cursor.fetchone()
    conn.close()
    return result is not None

# Function to handle user logout
def logout_user():
    st.session_state.logged_in = False
    st.success("You have been logged out.")
