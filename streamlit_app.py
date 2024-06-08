from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

#directories and path
THIS_DIR=Path(__file__).parent
CSS_FILE=THIS_DIR/"style"/"style.css"
ASSETS=THIS_DIR/"assets"
LOTTIE_ANIMATION=ASSETS/"animation_birthday.json"
# function to load and display animation
def load_lottie_animation(file_path):
    with open(file_path,"r") as f:
        return json.load(f)
# to apply effect of falling
def run_falling_animation():
    rain(emoji="🍰",font_size=20, falling_speed=5,animation_lenght="infinite")

#to display name
def get_person_name():
    query_parmas=st.experimental_get_query_params()
    return query_parmas.get("name",["Friend"])[0]
# page configuration
st.set_page_config(page_title="Happy Birthday",page_icon="🎂")
#run animmation
run_falling_animation()
#apply css
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
# personalized name
PERSON_NAME=get_person_name()
st.header(f" To my Friend {PERSON_NAME}! 🎂",anchor=False)
# display lottie animation
lottie_animation=load_lottie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation,key="lottie-birthday",height=300)
# personalized message to friend
st.markdown(
    f"Dear {PERSON_NAME}, wishing you a happy birthday to you ..."
)