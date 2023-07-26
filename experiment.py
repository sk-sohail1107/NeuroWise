import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image


def experimentt():
    DEFAULT_WIDTH = 80
    VIDEO_DATA = "https://youtu.be/_Um12_OlGgw"

    # st.set_page_config(layout="wide")

    width = st.sidebar.slider(
        label="Width", min_value=0, max_value=100, value=DEFAULT_WIDTH, format="%d%%"
    )

    width = max(width, 0.01)
    side = max((100 - width) / 2, 0.01)

    _, container, _ = st.columns([side, width, side])
    container.video(data=VIDEO_DATA)

