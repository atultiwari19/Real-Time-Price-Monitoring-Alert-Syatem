import streamlit as st
from PIL import Image

img = Image.open("./dashboard.jpg")
st.image(img, width=4000)

st.title("Real-Time Price Monitoring Alert System")

st.header("Daily Price Tracking")
st.header("Historical Storage")
st.header("Price Comparison")
st.header("Alert System for Price Changes")
st.header("Automated Pipeline")

st.markdown("Database Connectivity")

st.success("Proceed Successfully")

st.info("Find the formal information")

st.warning("You are going into a high-risk scenario")

st.error("Account has been blocked for 24 hours")

