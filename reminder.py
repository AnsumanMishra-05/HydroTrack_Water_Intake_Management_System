import streamlit as st
import datetime

def show_reminder():
    st.subheader("⏰ Hydration Reminder")

    reminder_time = st.time_input("Set a reminder time", datetime.time(9, 0))

    current_time = datetime.datetime.now().time()
    if current_time.hour == reminder_time.hour and current_time.minute == reminder_time.minute:
        st.warning("💧 Time to drink water!")

    st.info("Note: This reminder only checks the time when the page is refreshed. "
            "To get real reminders, you would need background processes or notifications.")
