import streamlit as st

def profile_data(dataset):
    if dataset is not None:
        st.subheader("Automated Data Analysis")
        st.info("Description of uploaded dataset")
        st.write(dataset.info())
        st.write(dataset.describe())
        st.info("Columns in dataset uploaded")
        st.write(dataset.columns)
    else:
        st.warning(":arrow_double_up: Upload Dataset first in Upload section")
