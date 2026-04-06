import streamlit as st

lang = ["Python", "JavaScript", "C++", "Java"]

st.title("Class Poll")
st.radio("What's your favorite programming language?", lang)

st.header("Current Results")

if st.button("Vote"):