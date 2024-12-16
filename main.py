import streamlit as st

# Set the title of the web page
st.title("Mature Audience Only 18+")

# Set a header
game = st.header("Hancock Vs. STL Today at 7pm")
# Text input for name
winner = st.text_input("Enter who you think will win:")
# Dropdown menu for selecting an option
options = ["Close Game", "Blowout"]
result = st.selectbox("Choose an option:", options)
# Slider for selecting a value
points = st.slider("How many points will Hancock make", 1, 100, 50)
# Submit button
if st.button("Done"):
    st.write(f"You think {winner} will win.")
    st.write(f"You think it will be a {result}")
    st.write(f"You think Hancock will make {points} points.")
# Additional information

# Footer

