import streamlit as st
import pandas as pd
import altair as alt
from database import get_water_logs

def show_analysis(username):
    st.subheader("Water Intake Analysis")

    logs = get_water_logs(username)

    if not logs:
        st.warning("No intake data available yet.")
        return

    df = pd.DataFrame(logs, columns=["amount", "date"])
    df["date"] = pd.to_datetime(df["date"]).dt.date

    # Show raw logs
    st.write("Raw Logs:")
    st.dataframe(df)

    # Group by date
    daily_summary = df.groupby("date", as_index=False)["amount"].sum()

    st.write("Grouped Daily Intake:")
    st.dataframe(daily_summary)

    # Bar Chart (better for single/multiple entries)
    chart = alt.Chart(daily_summary).mark_bar(color="#1f77b4").encode(
        x=alt.X("date:T", title="Date"),
        y=alt.Y("amount:Q", title="Water Intake (ml)"),
        tooltip=["date", "amount"]
    ).properties(
        width=700,
        height=400
    )

    st.altair_chart(chart)

    # Summary stats
    average = daily_summary["amount"].mean()
    total = daily_summary["amount"].sum()

    st.markdown(f"**Average Daily Intake (ml)**")
    st.markdown(f"### {average:.1f}")
    st.markdown(f"**Total Logged Intake (ml)**")
    st.markdown(f"### {int(total)}")
