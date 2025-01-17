from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain


#Directories and file paths
THIS_DIR=Path(__file__).parent
CSS_FILE=THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "animation_holiday.json"


def load_lottie_animation(file_path):
    with open(file_path,"r") as f:
        return json.load(f)
    
def run_snow_animation():
    rain(emoji="❄️", font_size=20, falling_speed=5,animation_length='infinite')

def get_person_name():
    query_params = st.experimental_get_query_params()
    return query_params.get("name",["Friends"])[0]

st.set_page_config(page_title="Happy Holidays", page_icon="🎄")

run_snow_animation()

with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

PERSON_NAME = get_person_name()
st.header(f"Happy Holidays, {PERSON_NAME}! 🎄", anchor=False)

lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, key="lottie-holiday", height =300)


st.markdown(
    f"Dear {PERSON_NAME}, wishing you a wonderfull holiday season filled with joy and peace. ✨"
)