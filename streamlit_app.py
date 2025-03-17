import streamlit as st
import json
import io

st.set_page_config(page_title="Blood Logistics Tool Input", layout="wide")

st.title("ONR Blood Mangement Support Tool")
st.sidebar.header("User Input")

# Create a dictionary to store user data
if "user_data" not in st.session_state:
    st.session_state.user_data = []
with st.form("user_form"):
    name = st.text_input("Enter your name:")
    platoonNum = st.number_input("Enter the corresponding platoon number:")
    currentCombatLevel = st.number_input("Enter the current comabt level:")
    predictedCompabtLevel = st.number_input("Enter predicted combat level")
    submit = st.form_submit_button("Submit")
    
    if submit:
        new_entry = {"name": name, "Platoon Number": platoonNum, "current comabt level": currentCombatLevel, "predicted comabt level": predictedCompabtLevel}
        st.session_state.user_data.append(new_entry)
        st.success("Data added successfully!")

# Display stored data
st.subheader("Stored User Data")
st.json(st.session_state.user_data)

# Convert data to JSON and provide a download link
if st.session_state.user_data:
    json_data = json.dumps(st.session_state.user_data, indent=4)
    json_file = io.BytesIO(json_data.encode())

    st.download_button(
        label="Download JSON File",
        data=json_file,
        file_name="user_data.json",
        mime="application/json"
    )
#st.title("User Input")
#st.headers
#x = st.text_input("Input 1: ")
#st.write(f"The first input is: {x}")
#st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")
#is_clicked = st.button("Click Me")
#st.write('##this is a title: ')
