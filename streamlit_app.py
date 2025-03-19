import streamlit as st
import json
import io

st.set_page_config(page_title="Blood Logistics Tool Input", layout="wide")

st.title("ONR Blood Management Support Tool")
st.sidebar.header("User Input")

# Initialize session state if not present
if "user_data" not in st.session_state:
    st.session_state.user_data = []

# Create the form
with st.form("blood_management_form"):
    name = st.text_input("Enter your name:")
    platoonNum = st.number_input("Enter the corresponding platoon number:", min_value=0)
    currentCombatLevel = st.number_input("Enter the current combat level:", min_value=0)
    predictedCombatLevel = st.number_input("Enter predicted combat level:", min_value=0)
    
    submit = st.form_submit_button("Submit")

# Handle form submission
if submit:
    new_entry = {
        "name": name,
        "Platoon Number": platoonNum,
        "Current Combat Level": currentCombatLevel,
        "Predicted Combat Level": predictedCombatLevel
    }
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
