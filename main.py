import streamlit as st

# Set page config as first Streamlit command
st.set_page_config(page_title="HydroTrack", layout="wide")

# Import after setting config
from auth import register_user, login_user
from profile import setup_profile
from logger import log_water_intake
from analysis import show_analysis
from reminder import show_reminder
from benefits import show_benefits
from style import set_custom_style

# Apply custom style
set_custom_style()

# App header
st.image("assets/logo.png", width=170)
st.title("HydroTrack - Water Intake Management System")

# Session state init
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "page_index" not in st.session_state:
    st.session_state.page_index = 0

# Pages list
pages = ["Login", "Register", "Profile", "Log Water Intake", "Analysis", "Reminder", "Benefits", "Logout"]

# Sidebar Navigation (manual override)
selected = st.sidebar.selectbox("Navigation", pages, index=st.session_state.page_index)
st.session_state.page_index = pages.index(selected)
current_page = pages[st.session_state.page_index]

# Page Routing
if current_page == "Register":
    st.subheader("Create Account")
    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")
    if st.button("Register"):
        if register_user(new_user, new_pass):
            st.success("Account created successfully. You can log in now.")
        else:
            st.error("Username already exists.")

elif current_page == "Login":
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login_user(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.page_index = pages.index("Profile")
            st.success(f"Welcome, {username}!")
            st.rerun()
        else:
            st.error("Invalid credentials.")

elif current_page == "Logout":
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.page_index = pages.index("Login")
    st.success("Logged out successfully.")
    st.rerun()

# Main Features
if st.session_state.logged_in:
    username = st.session_state.username

    if current_page == "Profile":
        setup_profile(username)

    elif current_page == "Log Water Intake":
        log_water_intake(username)

    elif current_page == "Analysis":
        show_analysis(username)

    elif current_page == "Reminder":
        show_reminder()

    elif current_page == "Benefits":
        show_benefits()

# Navigation buttons
if st.session_state.logged_in and current_page not in ["Login", "Register", "Logout"]:
    col1, col2 = st.columns([1, 6])
    with col1:
        if st.button("⬅ Back") and st.session_state.page_index > 0:
            st.session_state.page_index -= 1
            st.rerun()
    with col2:
        if st.button("Next ➡") and st.session_state.page_index < len(pages) - 1:
            st.session_state.page_index += 1
            st.rerun()