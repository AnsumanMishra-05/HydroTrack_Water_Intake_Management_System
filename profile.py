import streamlit as st
from database import connect_db  # ✅ Correct import

def create_profile_table():
    conn, cursor = connect_db()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS profile (
            username TEXT PRIMARY KEY,
            age INTEGER,
            weight REAL,
            activity_level TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_profile(username, age, weight, activity_level):
    create_profile_table()  # ✅ Ensure table exists
    conn, cursor = connect_db()
    cursor.execute("""
        INSERT OR REPLACE INTO profile (username, age, weight, activity_level)
        VALUES (?, ?, ?, ?)
    """, (username, age, weight, activity_level))
    conn.commit()
    conn.close()

def get_profile(username):
    create_profile_table()  # ✅ Ensure table exists
    conn, cursor = connect_db()
    cursor.execute("SELECT age, weight, activity_level FROM profile WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    return result

def setup_profile(username):
    st.subheader("Set Up Your Profile")
    profile = get_profile(username)

    if profile:
        age, weight, activity_level = profile
    else:
        age, weight, activity_level = 18, 60.0, "Low"

    age = st.number_input("Age", min_value=1, max_value=120, value=age)
    weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=weight)
    activity_level = st.selectbox("Activity Level", ["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(activity_level))

    if st.button("Save Profile"):
        save_profile(username, age, weight, activity_level)
        st.success("Profile saved successfully!")
