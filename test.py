import streamlit as st

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file:
    file_details = uploaded_file.read()
    st.write(file_details.decode("utf-8"))
