# streamlit_app.py
import os
os.environ["STREAMLIT_WATCH_USE_POLLING"] = "true"

import streamlit as st
from utils import load_data, save_data

st.set_page_config(page_title="PlantSync", layout="wide")

# ---- Theme Selector ----
theme = st.selectbox("Choose Theme", ["Light", "Midnight", "Spring Green", "Desert Tan", "Sunset Orange"])
custom_css = ""
if theme == "Midnight":
    custom_css = """
        <style>
        .stApp {
            background-color: #121212;
            color: #f0f0f0;
        }
        section[data-testid="stSidebar"] {
            background-color: #1a1a1a;
        }
        section[data-testid="stSidebar"] .css-1cpxqw2 {
            color: #f0f0f0;
        }
        h1, h2, h3, h4, h5, h6, .markdown-text-container {
            color: #f0f0f0 !important;
        }
        .stMarkdown p {
            color: #dcdcdc !important;
        }
        </style>
    """
elif theme == "Spring Green":
    custom_css = """
        <style>
        .stApp {
            background-color: #d5f5dc;
            color: #1e4620;
        }
        section[data-testid="stSidebar"] {
            background-color: #b8e6c2;
        }
        section[data-testid="stSidebar"] .css-1cpxqw2 {
            color: #1e4620;
        }
        h1, h2, h3, h4, h5, h6, .markdown-text-container {
            color: #1e4620 !important;
        }
        .stMarkdown p {
            color: #2c5f30 !important;
        }
        </style>
    """

elif theme == "Desert Tan":
    custom_css = """
        <style>
        .stApp {
            background-color: #f9f3df;
            color: #4a3620;
        }
        section[data-testid="stSidebar"] {
            background-color: #f3e8c9;
        }
        section[data-testid="stSidebar"] .css-1cpxqw2 {
            color: #4a3620;
        }
        h1, h2, h3, h4, h5, h6, .markdown-text-container {
            color: #5a3e1b !important;
        }
        .stMarkdown p {
            color: #5a3e1b !important;
        }
        </style>
    """

elif theme == "Sunset Orange":
    custom_css = """
        <style>
        .stApp {
            background-color: #fff2e6;
            color: #332211;
        }
        section[data-testid="stSidebar"] {
            background-color: #ffe5cc;
        }
        section[data-testid="stSidebar"] .css-1cpxqw2 {
            color: #553311;
        }
        h1, h2, h3, h4, h5, h6, .markdown-text-container {
            color: #cc5500 !important;
        }
        .stMarkdown p {
            color: #553311 !important;
        }
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
