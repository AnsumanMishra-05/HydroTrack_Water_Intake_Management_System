import streamlit as st

def set_custom_style():
    st.markdown("""
        <style>
            /* Background color */
            .stApp {
                background-color: #E3F2FD;
                font-family: 'Segoe UI', sans-serif;
            }

            /* Title styling */
            h1, h2, h3 {
                color: #0D47A1;
            }

            /* Button styling */
            div.stButton > button {
                background-color: #2196F3;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 16px;
                transition: 0.3s;
            }

            div.stButton > button:hover {
                background-color: #1976D2;
                transform: scale(1.03);
            }

            /* Input box styling */
            .stTextInput > div > div > input {
                border-radius: 8px;
                border: 1px solid #90CAF9;
                padding: 8px;
            }

            /* Sidebar styling */
            .css-1d391kg {  /* Sidebar class (Streamlit may change this over time) */
                background-color: #BBDEFB;
            }

        </style>
    """, unsafe_allow_html=True)
