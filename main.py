import streamlit as st

cols = st.columns(3)
with cols[0]:
    a = st.text_input('Name')
with cols[1]:
    b = st.text_input('Year')
with cols[2]:
    c = st.text_input('Other field')

file = st.file_uploader("select file", )
print(cols)

st.button("submit", disabled=True)