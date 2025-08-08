import json
from pathlib import Path

DATA_FILE = Path("data/plant_data.json")

def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    DATA_FILE.parent.mkdir(exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_theme_css(theme):
    if theme == "Midnight":
        return """<style>
            .stApp { background-color: #1e1e24; color: #f0f0f0; }
            section[data-testid="stSidebar"] { background-color: #262630; }
            section[data-testid="stSidebar"] * { color: #f0f0f0 !important; transition: all 0.3s ease; }
            .css-1d391kg:hover, .css-16idsys:hover { background-color: #33334d !important; border-radius: 5px; }
            .css-17lntkn { background-color: #40405a !important; border-left: 4px solid #cc5500; border-radius: 5px; }
            h1, h2, h3, h4, h5, h6, .markdown-text-container { color: #ffffff !important; }
            .stMarkdown p { color: #dcdcdc !important; }
        </style>"""
    # Repeat for other themes like "Sunset Orange", etc...
    return ""
