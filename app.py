import streamlit as st
#from streamlit_option_menu import option_menu
from PIL import Image
import home
import classification


st.set_page_config(page_title="NeuroWise",layout="wide", page_icon=":brain:")


st.markdown("""<style>
.appview-container .main .block-container{{
        padding-top: {padding_top}rem;    }}
</style>""", unsafe_allow_html=True)


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.sidebar.title(" :brain: NeuroWise")
selected = st.sidebar.radio(
    label="",
    options=["🏛️ Home", "🔁 Classification"],
    
)
# selected = st.sidebar.che(
#     menu_title=None,
#     options=["Home", "Classification"],
#     icons=["house", "repeat"],
#     # menu_icon="cast",
#     default_index=0,
#     orientation="horizontal",
# )

if selected == "🏛️ Home":
    home.homee()

if selected == "🔁 Classification":
    classification.classificationn()

# if selected=="Experiment":
#     experiment.experimentt()

    