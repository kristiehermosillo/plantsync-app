import streamlit as st
from utils import load_data, save_data
from datetime import datetime

st.title("📝 Plant Log")

data = load_data()

if not data:
    st.info("No plants added yet.")
else:
    plant_names = [plant["name"] for plant in data]
    selected_plant = st.selectbox("Select a plant to view or update log", plant_names)

    plant = next(p for p in data if p["name"] == selected_plant)

    st.markdown(f"**Tags:** {', '.join(plant['tags'])}")
    st.markdown(f"**Next Watering:** {plant['next_water']}")
    st.markdown(f"**Next Pruning:** {plant['next_prune']}")
    st.markdown(f"**Notes:** {plant['notes']}")

    if plant.get("photo"):
        st.image(f"data/photos/{plant['photo']}", width=200)

    st.subheader("Add a new log entry")

    with st.form("log_entry"):
        log_note = st.text_area("What did you observe or do?")
        submitted = st.form_submit_button("Add to Log")

        if submitted and log_note:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            entry = f"[{timestamp}] {log_note}"
            plant["history"].append(entry)
            save_data(data)
            st.success("Log updated.")

    if plant["history"]:
        st.subheader("Log History")
        for entry in reversed(plant["history"]):
            st.markdown(f"- {entry}")
