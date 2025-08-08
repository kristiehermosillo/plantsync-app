import streamlit as st
from utils import load_data, save_data
from utils import get_theme_css

theme = st.session_state.get("theme", "Light")
custom_css = get_theme_css(theme)
st.markdown(custom_css, unsafe_allow_html=True)

st.title("⚙️ Settings")

data = load_data()

if not data:
    st.info("No plants found.")
else:
    plant_names = [p["name"] for p in data]
    selected = st.selectbox("Select a plant to edit or delete", plant_names)

    plant = next(p for p in data if p["name"] == selected)

    with st.form("edit_plant"):
        new_name = st.text_input("Edit Plant Name", value=plant["name"])
        new_tags = st.text_input("Edit Tags (comma separated)", value=", ".join(plant["tags"]))
        new_notes = st.text_area("Edit Notes", value=plant["notes"])
        submit = st.form_submit_button("Save Changes")

        if submit:
            plant["name"] = new_name
            plant["tags"] = [t.strip() for t in new_tags.split(",") if t.strip()]
            plant["notes"] = new_notes
            save_data(data)
            st.success("Plant updated!")

    if st.button("🚨 Delete This Plant"):
        data = [p for p in data if p["name"] != selected]
        save_data(data)
        st.warning(f"{selected} has been deleted.")
