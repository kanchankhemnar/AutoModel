import streamlit as st
import pandas as pd
import os
import time
from supervised.automl import AutoML
import streamlit.components.v1 as components
from PIL import Image
# from ydata_profiling import ProfileReport


# from ydata_profiling import ProfileReport
# from streamlit_pandas_profiling import st_profile_report

st.set_page_config("AutoModel","🤖",layout="wide")
st.title("AutoML dashboard 📊📉")

with st.sidebar:
  st.image("sidebar_image.png")
  st.title("AutoModel")
  st.info("Follow below steps to create and train your own ML model over custom dataset.")
  choice = st.radio("Navigation",["Upload","Profiling","Train","Download "])

dataset = None

if os.path.exists("uploaded_dataset.csv"):
  uploaded_dataset = pd.read_csv("uploaded_dataset.csv")
  dataset = pd.DataFrame(uploaded_dataset)

if choice=="Upload":
  st.markdown("## :file_folder: Upload your dataset in csv format")
  uploaded_file = st.file_uploader("")
  if uploaded_file:
    csv_file = pd.read_csv(uploaded_file)
    dataset = pd.DataFrame(csv_file,index=None)
    st.markdown("#### Dataset Content")
    st.write(dataset)
    csv_file.to_csv("uploaded_dataset.csv",index=None)
    

  elif dataset is not None:
    st.markdown("####  Dataset Preview")
    st.write(dataset)

    
if choice=="Profiling":
  if dataset is not None:
    st.subheader("Automated Data Analysis")
    st.info("Description of uploaded dataset")
    st.write(dataset.info())
    st.write(dataset.describe())
    st.info("Columns in dataset uploaded")
    st.write(dataset.columns)
    # profile = ProfileReport(uploaded_dataset)
    # st.write(profile)


  else:
    st.warning(":arrow_double_up: Upload Dataset first in Upload section")

model_choice = None
inner_model_choice = None

if choice=="Train":

  if model_choice is None:
    st.info("#### Select ML Task")
    model_choice = st.selectbox(label="",options=["Classification","Regression","Clustering","Apriori Algorithm"],placeholder="select")
  
  
  if model_choice == "Regression":

    # inner_model_choice = st.selectbox(label="Select Regression type",options=["Linear Regression","Multiple Regression","Polynomial Regression","Random Forest","Decision Tree"])

    # if dataset is not None:
      target_feature = st.selectbox("Select target feature",dataset.columns)

      if st.button("Run AutoModel"):
        X = dataset.drop(columns=[target_feature])
        y = dataset[target_feature]
        automl = AutoML(
          mode="Compete",
          ml_task="regression",
          total_time_limit=60,
          results_path="automl_results",
          explain_level=0
        )   

        with st.spinner("Executing :rocket: "):
          automl.fit(X,y)
          # time.sleep()
            
        st.success("✅ Models executed successfully!")
        # st.info("Report")
        # leaderboard_path = "automl_results/leaderboard.csv"
        # if os.path.exists(leaderboard_path):
        #     st.markdown("### ")
        #     leaderboard_df = pd.read_csv(leaderboard_path)
        #     st.markdown("### 🏆 Leaderboard")
        #     st.dataframe(leaderboard_df)

        # # Load and display performance scatter plot
        # scatter_path = "automl_results/ldb_performance.png"
        # if os.path.exists(scatter_path):
        #     st.markdown("### 📈 Performance Plot")
        #     scatter_img = Image.open(scatter_path)
        #     st.image(scatter_img, use_column_width=800)
        report = automl.report()
        components = components.html(report.data,height=1000,scrolling=True)

    


if choice=="Download":
  pass