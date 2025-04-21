import streamlit as st
import pandas as pd
import os

uploaded_file = None

def upload_dataset(dataset):
    st.markdown("## :file_folder: Upload your dataset in csv format")

    uploaded_file = st.file_uploader("")

    sample_datasets = {
    "Iris Dataset (classification)" : "sampleDatasets/iris.csv",
    "Salary Dataset (linear regression)" : "sampleDatasets/salaryData.csv",
    "Student Percentage Prediction (polynomial regression)" : "sampleDatasets/studentPercentagePrediction.csv",
    "Gender Dataset (classification)" : "sampleDatasets/genderClassification.csv",
    "House Price Prediction (regression)" : "sampleDatasets/housePricePrediction.csv",
    "Student Grade System (classification)" : "sampleDatasets/studentGradeClassification.csv",

    }
    
    sample_file = None

    if uploaded_file is None:
        st.markdown("### :file_folder: Select sample datasets")
        sample_file = st.selectbox("select",options=[None]+ list(sample_datasets.keys()),index=None,placeholder="Choose sample dataset")
        if sample_file is not None:
            uploaded_file = sample_datasets[sample_file]
        
    if uploaded_file:
        csv_file = pd.read_csv(uploaded_file)
        dataset = csv_file
        st.markdown("#### Dataset Preview")
        st.write(dataset)
        csv_file.to_csv("uploaded_dataset.csv", index=None)
    elif dataset is not None:
        st.markdown("####  Dataset Preview")
        st.write(dataset)
    return dataset


 