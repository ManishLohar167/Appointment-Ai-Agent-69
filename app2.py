import streamlit as st
import requests

st.set_page_config(page_title="Appointment Booking", layout="centered")
st.title("📅 Appointment Booking Chatbot")

name = st.text_input("Your Name")
email = st.text_input("Your Email")
date = st.date_input("Select Appointment Date")
time = st.time_input("Preferred Time")

if st.button("📤 Book Appointment"):
    data = {
        "name": name,
        "email": email,
        "date": str(date),
        "time": str(time)
    }
    try:
        resp = requests.post("https://appointment-backend-1-x8mo.onrender.com/book", json=data)
        if resp.status_code == 200:
            st.success("✅ Appointment booked successfully!")
        else:
            st.error("❌ Failed to book appointment.")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")