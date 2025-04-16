import streamlit as st
import pandas as pd

def upload_dataset(dataset):
    st.markdown("## :file_folder: Upload your dataset in csv format")
    uploaded_file = st.file_uploader("")
    if uploaded_file:
        csv_file = pd.read_csv(uploaded_file)
        dataset = csv_file
        st.markdown("#### Dataset Content")
        st.write(dataset)
        csv_file.to_csv("uploaded_dataset.csv", index=None)
    elif dataset is not None:
        st.markdown("####  Dataset Preview")
        st.write(dataset)
    return dataset
