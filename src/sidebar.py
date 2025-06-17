import streamlit as st
from src import auth
def sidebar_content():
    st.title("AutoModel")
    st.info("Follow below steps to create and train your own ML model over custom dataset.")
    global choice
    choice = st.radio("Navigation", ["Login","Upload", "Profiling", "Train", "Download"])

