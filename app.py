# streamlit_app.py

import streamlit as st

# Title of the app
st.title("Simple Greeting App")

# Text input
name = st.text_input("Enter your name:")

# Button and response
if st.button("Greet"):
    if name:
        st.success(f"Hello, {name}! 👋")
    else:
        st.warning("Please enter your name first.")
