import streamlit as st
from utils import load_data, save_data
from datetime import datetime, timedelta

# apply CSS stored by the main page
st.markdown(st.session_state.get("custom_css", ""), unsafe_allow_html=True)

st.title("🌱 Add a New Plant")

data = load_data()

with st.form("add_plant"):
    name = st.text_input("Plant Name")
    tag = st.text_input("Tags (comma-separated, like 'succulent, outdoor')")
    water_freq = st.number_input("Water every __ days", min_value=1, max_value=90, value=7)
    prune_freq = st.number_input("Prune every __ days", min_value=0, max_value=180, value=30)
    notes = st.text_area("Initial Notes")
    photo = st.file_uploader("Upload a photo", type=["png", "jpg", "jpeg"])

    submitted = st.form_submit_button("Add Plant")

    if submitted and name:
        plant = {
            "name": name,
            "tags": [t.strip() for t in tag.split(",") if t.strip()],
            "water_freq": water_freq,
            "prune_freq": prune_freq,
            "notes": notes,
            "next_water": (datetime.now() + timedelta(days=water_freq)).strftime("%Y-%m-%d"),
            "next_prune": (datetime.now() + timedelta(days=prune_freq)).strftime("%Y-%m-%d"),
            "photo": photo.name if photo else None,
            "history": []
        }
        data.append(plant)
        save_data(data)

        if photo:
            with open(f"data/photos/{photo.name}", "wb") as f:
                f.write(photo.getbuffer())

        st.success(f"{name} has been added!")
