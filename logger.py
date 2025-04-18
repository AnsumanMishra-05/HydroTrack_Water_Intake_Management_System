import streamlit as st
import datetime
from database import insert_water_log

def log_water_intake(username):
    st.subheader("Log Water Intake")

    # Input amount of water in ml
    amount = st.number_input("Enter amount of water consumed (ml):", min_value=50, max_value=2000, step=50)

    if st.button("Log Intake"):
        if amount:
            date = datetime.date.today().strftime("%Y-%m-%d")
            insert_water_log(username, amount, date)
            st.success(f"{amount}ml of water logged successfully for {date}.")
        else:
            st.warning("Please enter a valid amount.")
