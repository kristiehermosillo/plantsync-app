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

def get_theme_css(theme: str) -> str:
    if theme == "Midnight":
        return """
        <style>
        .stApp { background-color: #1e1e24; color: #f0f0f0; }
        section[data-testid="stSidebar"] { background-color: #262630; }
        section[data-testid="stSidebar"] * { color: #f0f0f0 !important; transition: all 0.3s ease; }
        .css-1d391kg:hover, .css-16idsys:hover { background-color: #33334d !important; border-radius: 6px; }
        .css-17lntkn { background-color: #40405a !important; border-left: 4px solid #cc5500; border-radius: 6px; }
        h1, h2, h3, h4, h5, h6, .markdown-text-container { color: #ffffff !important; }
        .stMarkdown p { color: #dcdcdc !important; }
        </style>
        """
    if theme == "Spring Green":
        return """
        <style>
        .stApp { background-color: #d5f5dc; color: #1e4620; }
        section[data-testid="stSidebar"] { background-color: #b8e6c2; }
        section[data-testid="stSidebar"] * { color: #1e4620 !important; transition: all 0.3s ease; }
        .css-1d391kg:hover, .css-16idsys:hover { background-color: #a8dab4 !important; border-radius: 6px; }
        h1, h2, h3, h4, h5, h6, .markdown-text-container { color: #1e4620 !important; }
        .stMarkdown p { color: #2c5f30 !important; }
        </style>
        """
    if theme == "Desert Tan":
        return """
        <style>
        .stApp { background-color: #f9f3df; color: #4a3620; }
        section[data-testid="stSidebar"] { background-color: #f3e8c9; }
        section[data-testid="stSidebar"] * { color: #4a3620 !important; transition: all 0.3s ease; }
        .css-1d391kg:hover, .css-16idsys:hover { background-color: #e8dbba !important; border-radius: 6px; }
        h1, h2, h3, h4, h5, h6, .markdown-text-container { color: #5a3e1b !important; }
        .stMarkdown p { color: #5a3e1b !important; }
        </style>
        """
    if theme == "Sunset Orange":
        return """
        <style>
        .stApp { background-color: #fff2e6; color: #332211; }
        section[data-testid="stSidebar"] { background-color: #ffe5cc; }
        section[data-testid="stSidebar"] * { color: #553311 !important; transition: all 0.3s ease; }
        .css-1d391kg:hover, .css-16idsys:hover { background-color: #ffd6b3 !important; border-radius: 6px; }
        h1, h2, h3, h4, h5, h6, .markdown-text-container { color: #cc5500 !important; }
        .stMarkdown p { color: #553311 !important; }
        </style>
        """
    if theme == "Light":
        return """
        <style>
        .stApp { background-color: #ffffff; color: #000000; }
        section[data-testid="stSidebar"] { background-color: #f0f2f6; }
        section[data-testid="stSidebar"] * { color: #000000 !important; }
        h1, h2, h3, h4, h5, h6, .markdown-text-container { color: #000000 !important; }
        .stMarkdown p { color: #333333 !important; }
        </style>
        """
    return ""
