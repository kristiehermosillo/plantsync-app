import streamlit as st
from utils import load_data
from datetime import datetime

st.title("📆 Calendar View")

data = load_data()

if not data:
    st.info("No plants to show.")
else:
    view_option = st.selectbox("Show tasks for:", ["Watering", "Pruning", "Both"])

    today = datetime.today()
    st.subheader(f"Upcoming Tasks (after {today.strftime('%Y-%m-%d')})")

    for plant in data:
        show = False
        if view_option == "Watering" or view_option == "Both":
            next_water = datetime.strptime(plant["next_water"], "%Y-%m-%d")
            if next_water >= today:
                show = True
                st.markdown(f"🌊 **{plant['name']}** — Water on `{plant['next_water']}`")
        if view_option == "Pruning" or view_option == "Both":
            next_prune = datetime.strptime(plant["next_prune"], "%Y-%m-%d")
            if next_prune >= today:
                show = True
                st.markdown(f"✂️ **{plant['name']}** — Prune on `{plant['next_prune']}`")

        if not show:
            st.markdown(f"✅ **{plant['name']}** has no upcoming tasks.")
