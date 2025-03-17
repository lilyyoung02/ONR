import streamlit as st

st.set_page_config(page_title="Blood Logistics Tool Input", layout="wide")

st.title("ONR Blood Mangement Support Tool")
st.sidebar.header("User Input")

# Create a dictionary to store user data
if "user_data" not in st.session_state:
    st.session_state.user_data = []

#st.title("User Input")
#st.headers
#x = st.text_input("Input 1: ")
#st.write(f"The first input is: {x}")
#st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")
#is_clicked = st.button("Click Me")
#st.write('##this is a title: ')
