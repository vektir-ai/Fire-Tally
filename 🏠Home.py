import streamlit as st
import base64
from pathlib import Path

def landing_page_styles():
    return """
    <style>
        header {
            visibility: hidden;
        }
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
        }
        footer {visibility: hidden;}
        [data-testid="stSidebar"] {
        visibility: hidden;
        }
        [data-testid="collapsedControl"] {
            display: none;
        }

    </style>
    """

st.set_page_config(
    page_title="Fire Tally",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed",
)


st.markdown(landing_page_styles(), unsafe_allow_html=True)

# Containers ----------------------
sL, header, sR = st.columns([0.25, 0.5, 0.25])
sL1, getStarted, sR1 = st.columns([0.4, 0.2, 0.4])
sL2, hero, sR2 = st.columns([0.3, 0.4, 0.3])

with header:
    hero_section = """</br><h2 style='text-align: center;'>Welcome to the🔥Fire Tally App</h2></hr>
        <p style='text-align: center; color:gray; font-size:110%;'>
        Simplify the way you create and manage pipe tallies on your drilling rig. Fire-Tally offers an intuitive, 
        user-friendly interface with editable tables tailored for drilling professionals.
        Enhance efficiency and keep your operations running smoothly with our seamless pipe tally solution for
      <b style='text-align: center; color:gray; font-size:150%;'> FREE!</b>  </p></br>
    """
    st.markdown(hero_section, unsafe_allow_html=True)

with getStarted:
    st.button('Get Started', type='primary', on_click="", use_container_width=True )

with hero:
    st.image('assets/fire-tally.png', use_column_width=True)