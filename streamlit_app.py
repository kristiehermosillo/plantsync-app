# streamlit_app.py
import os
os.environ["STREAMLIT_WATCH_USE_POLLING"] = "true"

import streamlit as st
from utils import load_data, save_data

st.set_page_config(page_title="PlantSync", layout="wide")

# ---- Theme Selector ----
theme = st.selectbox("Choose Theme", ["Light", "Dark", "Spring Green", "Desert Tan"])
custom_css = ""
if theme == "Dark":
    custom_css = """
        <style>
        body { background-color: #1e1e1e; color: white; }
        .stApp { background-color: #1e1e1e; }
        </style>
    """
elif theme == "Spring Green":
    custom_css = """
        <style>
        .stApp { background-color: #d5f5dc; }
        </style>
    """
elif theme == "Desert Tan":
    custom_css = """
        <style>
        .stApp { background-color: #f9f3df; }
        </style>
    """

st.markdown(custom_css, unsafe_allow_html=True)

st.title("🌿 PlantSync Dashboard")

data = load_data()

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Upcoming Tasks")
    for plant in data:
        st.markdown(f"**{plant['name']}** - Next Watering: {plant['next_water']} 🌱")

with col2:
    st.subheader("Plant Summary")
    st.metric("Total Plants", len(data))
