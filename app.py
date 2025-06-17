import streamlit as st
import pandas as pd
import os
from src import upload, train, download, sidebar ,profiling ,auth

st.set_page_config("AutoModel", "🤖", layout="wide")
st.title("AutoML dashboard 📊📈")

with st.sidebar:
    st.image("sidebar_image.png")
    sidebar.sidebar_content()

dataset = None

if os.path.exists("uploaded_dataset.csv"):
    uploaded_dataset = pd.read_csv("uploaded_dataset.csv")
    dataset = pd.DataFrame(uploaded_dataset)

if "user" not in st.session_state:
    st.session_state.user = None

# Show login if not logged in


choice = sidebar.choice

if choice == "Upload":
    dataset = upload.upload_dataset(dataset)

elif choice == "Profiling":
    profiling.profile_data(dataset)

elif choice == "Train":
    train.train_model(dataset)

elif choice == "Download":
    download.download_models()

elif choice == "Login":
    if not st.session_state.user:
        auth.login_page()
    else:
        auth.logout_button()
