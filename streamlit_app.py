import streamlit as st
import json
import io

st.set_page_config(page_title="Blood Logistics Tool Input", layout="wide")

st.title("ONR Blood Management Support Tool")
st.sidebar.header("User Input")

# Ensure session state for user data
if "user_data" not in st.session_state:
    st.session_state.user_data = []

# Create the form
with st.form("blood_management_form"):
    simulation_days = st.number_input("Length of Simulation in Days:", min_value=1)
    med_log_company = st.number_input("Medical Logistics Company ID:", min_value=1)
    blood_inventory = st.number_input("Fresh Whole Blood Inventory on Hand (pints):", min_value=0)

    # Transportation schedule dropdowns
    st.markdown("### Transportation Schedule")
    transport_day = st.selectbox("Select Day:", options=[
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ])
    transport_time = st.time_input("Select Military Time:")
    transport_frequency = st.selectbox("Select Frequency:", options=[
        "Daily", "Weekly", "Bi-weekly", "Monthly"
    ])

    # Number of platoons
    num_med_platoons = st.number_input("Number of Medical Platoons:", min_value=0, step=1)

    # Dynamic input for each platoon's ID, size, location, and conflict likelihood
    platoon_data = []
    for i in range(int(num_med_platoons)):
        st.markdown(f"### Platoon {i + 1}")
        platoon_id = st.number_input(f"Enter ID for Platoon {i + 1} (Integer):", format="%d", step=1, key=f"platoon_id_{i}")
        platoon_size = st.number_input(f"Enter Size (people) for Platoon {i + 1}:", min_value=1, key=f"platoon_size_{i}")
        latitude = st.number_input(f"Enter Latitude for Platoon {i + 1}:", format="%.6f", key=f"latitude_{i}")
        longitude = st.number_input(f"Enter Longitude for Platoon {i + 1}:", format="%.6f", key=f"longitude_{i}")
        conflict_likelihood = st.slider(
            f"Likelihood of Conflict Tomorrow (0–5) for Platoon {i + 1} - 0: no conflict, 1: slight chance of conflict or training accident, 2: medium chance of conflict or training accident, 3: 50/50 chance of experiencing conflict, 4: high chance of light conflict, low chance of extreme conflict , 5: will experience high amounts of conflict",
            min_value=0, max_value=5, value=0, step=1, key=f"conflict_{i}"
        )
        platoon_data.append({
            "Platoon ID": int(platoon_id),
            "Platoon Size": platoon_size,
            "Latitude": latitude,
            "Longitude": longitude,
            "Conflict Likelihood": conflict_likelihood
        })

    submit = st.form_submit_button("Submit")

# Process form submission
if submit:
    if all([simulation_days, med_log_company, blood_inventory]) and all(
            p["Platoon ID"] is not None and
            p["Platoon Size"] and
            p["Latitude"] is not None and
            p["Longitude"] is not None
            for p in platoon_data):
        new_entry = {
            "Length of Simulation in Days": simulation_days,
            "Medical Logistics Company": med_log_company,
            "Fresh Whole Blood Inventory on Hand (pints)": blood_inventory,
            "Transportation Schedule": {
                "Day": transport_day,
                "Time": transport_time.strftime("%H:%M"),
                "Frequency": transport_frequency
            },
            "Number of Medical Platoons": num_med_platoons,
            "Platoons": platoon_data
        }
        st.session_state.user_data.append(new_entry)
        st.success("Data added successfully!")
    else:
        st.error("Please fill in all required fields for each platoon.")

# Display stored data
st.subheader("Stored User Data")
if st.session_state.user_data:
    st.json(st.session_state.user_data)

    # Convert data to JSON and provide a download link
    json_data = json.dumps(st.session_state.user_data, indent=4)
    json_file = io.BytesIO(json_data.encode())

    st.download_button(
        label="Download JSON File",
        data=json_file,
        file_name="user_data.json",
        mime="application/json"
    )
