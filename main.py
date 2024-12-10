import streamlit as st
st.write("Hello, World!")

st.title("My name is chicken ")
st.header("I am 18 years old")
st.subheader("Sub-header")

goon_count = st.button("Gooning Button")
st.write(f"you have gooned {goon_count} times ")

st.slider("Value", 1, 100, 50)