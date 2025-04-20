import streamlit as st
from supervised.automl import AutoML
import streamlit.components.v1 as component
from Regression import linearRegression, multipleRegression, polynomialRegression, randomForest, decisionTreeRegression
from Classification import binaryClassification,decisionTree,knn,logisticRegression,naiveBayes,svm
import shutil
from datetime import datetime
import os

def train_model(dataset):
    if dataset is None:
        st.warning(":arrow_double_up: Upload Dataset first")
        return

    st.info("#### Select ML Task")
    ml_task = st.selectbox(label="", options=["Select","Classification", "Regression"], placeholder="select")

    # Regression
    
    if ml_task == "Regression":
        model_choice = st.selectbox("Select Model",["Choose","All Models","Linear Regression","Multiple Regression","Polynomial Regression","Random Forest Regression","Decision Tree Regression"])

        target_feature = "Select"

        if(model_choice is not "Choose"):
            target_feature = st.selectbox("Select target feature",["Select"] + list(dataset.columns))

        # Automodel
        if model_choice == "All Models":
            st.info("This Automodel will run all possible models for regression through MLJar automated Machine learning.")


            if st.button("Run AutoModel"):
                if (target_feature == "Select"):
                    st.warning("Please select a target column to continue.")
                else:
                    X = dataset.drop(columns=[target_feature])
                    y = dataset[target_feature]

                    base_dir = "automl_results_regression"  
                    os.makedirs(base_dir, exist_ok=True)

                    results_path = os.path.join(base_dir, target_feature)

                    # Delete old results if they exist
                    if os.path.exists(results_path):
                        shutil.rmtree(results_path)

                    automl = AutoML(
                        mode="Compete",
                        ml_task="regression",
                        total_time_limit=60,
                        results_path=results_path,
                        explain_level=0
                    )

                    with st.spinner("Executing 🚀..."):
                        automl.fit(X, y)

                    st.success("✅ Model training completed!")
                    report = automl.report()
                    components = component.html(report.data,height=1000,scrolling=True)

        # Custom Models

        if model_choice == "Linear Regression":
            linearRegression.run_linear_regression(dataset, target_feature)

        elif model_choice == "Multiple Regression":
            multipleRegression.run_multiple_regression(dataset, target_feature)

        elif model_choice == "Polynomial Regression":
            polynomialRegression.run_polynomial_regression(dataset, target_feature)

        elif model_choice == "Random Forest Regression":
            randomForest.run_random_forest(dataset, target_feature)

        elif model_choice == "Decision Tree Regression":
            decisionTreeRegression.run_decision_tree(dataset, target_feature)

    if ml_task == "Classification":
        model_choice = st.selectbox("Select Model", ["Choose","Binary Classification","Multiclass Classification", "Logistic Regression", "K-Nearest Neighbors", "Support Vector Machine", "Naive Bayes", "Decision Tree Classifier"])

        target_feature = "Select"

        if model_choice != "Choose":
           
            target_feature = st.selectbox("Select target feature", ["Select" ]+ list(dataset.columns))

        # Automodel
        if model_choice == "Binary Classification" or model_choice == "Multiclass Classification":
            if model_choice == "Binary Classification":
                ml_task = "binary_classification" 
            else:
                ml_task="multiclass_classification"
            st.info(f"This Automodel will run all possible models for classification through MLJar automated Machine learning.")

            if st.button("Run AutoModel"):
                if target_feature == "Select":
                    st.warning("Please select a target column to continue.")
                else:
                    X = dataset.drop(columns=[target_feature])
                    y = dataset[target_feature]

                    base_dir = "automl_results_classification"  
                    os.makedirs(base_dir, exist_ok=True)

                    results_path = os.path.join(base_dir, target_feature)

                    # Delete old results if they exist
                    if os.path.exists(results_path):
                        shutil.rmtree(results_path)


                    automl = AutoML(
                        mode="Compete",
                        ml_task=ml_task,
                        total_time_limit=60,
                        results_path=results_path,
                        explain_level=0
                    )

                    with st.spinner("Executing 🚀..."):
                        automl.fit(X, y)

                    st.success("✅ Model training completed!")
                    report = automl.report()
                    components = component.html(report.data, height=1000, scrolling=True)

        # Custom Models

        if  target_feature is not "Select" :
            if model_choice == "Logistic Regression":
                logisticRegression.run_logistic_regression(dataset, target_feature)

            elif model_choice == "K-Nearest Neighbors":
                knn.run_knn(dataset, target_feature)

            elif model_choice == "Support Vector Machine":
                svm.run_svm(dataset, target_feature)

            elif model_choice == "Naive Bayes":
                naiveBayes.run_naive_bayes(dataset, target_feature)

            elif model_choice == "Decision Tree Classifier":
                decisionTree.run_decision_tree(dataset, target_feature)
        elif model_choice is not "Choose":
            st.warning("Select target feature to proceed")
