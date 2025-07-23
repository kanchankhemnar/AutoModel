def infer_task_type(target_series):
    if target_series is None:
        return
    import pandas as pd
    unique_values = target_series.nunique()
    if target_series.dtype == 'object' or unique_values < 20:
        return "Classification"
    elif pd.api.types.is_numeric_dtype(target_series):
        return "Regression"
    else:
        return "unknown"

def train_model(dataset):
    import streamlit as st
    from supervised.automl import AutoML
    import streamlit.components.v1 as component
    from ml.Regression import  regressionCodeTemplate
    from ml.Classification import classificationCodeTemplate
    import shutil
    import os
    if dataset is None:
        st.warning(":arrow_double_up: Upload Dataset first")
        return
    
    st.info("## Select ML Task")
    ml_task = st.selectbox(label="", options=["Classification", "Regression"],index=None ,placeholder="Select")

    model_choice=None

    # Regression
    
    if ml_task == "Regression":
        model_choice = st.selectbox("Select Model",["All Models","Linear Regression","Multiple Regression","Polynomial Regression","Random Forest Regression","Decision Tree Regression"],index=None,placeholder="Choose Model")



        target_feature = None


        target_feature = st.selectbox("Select target feature", list(dataset.columns) , index=None,placeholder="Select")

        if (target_feature is not None):
            inferred_task = infer_task_type(dataset[target_feature])

            if (target_feature is not None and inferred_task != ml_task):
                st.error(f"⚠️ Your selected task is '{ml_task}', but the data looks like a '{inferred_task}' task. Please select '{inferred_task}'.")
                st.stop()

        # Automodel
        if model_choice == "All Models":
            st.info("This Automodel will run all possible models for regression through MLJar automated Machine learning.")
            st.warning("Note : MLJar takes time to load. Please wait for few seconds.")


            if st.button("Run AutoModel"):
                if (target_feature == None):
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
        if (target_feature is not None and model_choice is not None):
            if(st.button("Run Model")):
                if model_choice == "Linear Regression":
                    regressionCodeTemplate.run_regression(dataset, target_feature, model_choice , f"📈{model_choice}")

                elif model_choice == "Multiple Regression":
                    regressionCodeTemplate.run_regression(dataset, target_feature, model_choice , f"📈{model_choice}")

                elif model_choice == "Polynomial Regression":
                    regressionCodeTemplate.run_regression(dataset, target_feature, model_choice , f"📈{model_choice}")

                elif model_choice == "Random Forest Regression":
                    regressionCodeTemplate.run_regression(dataset, target_feature , model_choice , f"🌲{model_choice}")

                elif model_choice == "Decision Tree Regression":
                    regressionCodeTemplate.run_regression(dataset, target_feature , model_choice , f"🌲{model_choice}")

    if ml_task == "Classification":
        model_choice = st.selectbox("Select Model", ["Binary Classification","Multiclass Classification", "Logistic Regression", "K-Nearest Neighbors", "Support Vector Machine", "Naive Bayes", "Decision Tree Classifier"],index=None,placeholder="Choose Model")

        target_feature = None

        # if model_choice != None:
        #     guidanceButton.render_info_button(ml_task,model_choice)
        target_feature = st.selectbox("Select target feature", [None]+ list(dataset.columns),index=None,placeholder="Select")

        if (target_feature is not None):
            inferred_task = infer_task_type(dataset[target_feature])

            if (target_feature is not None and inferred_task != ml_task):
                st.error(f"⚠️ Your selected task is '{ml_task}', but the data looks like a '{inferred_task}' task. Please select '{inferred_task}'.")
                st.stop()

        # Automodel
        mljar_task = False
        if model_choice == "Binary Classification" or model_choice == "Multiclass Classification":
            mljar_task = True
            if model_choice == "Binary Classification":
                ml_task = "binary_classification" 
            else:
                ml_task="multiclass_classification"
            st.info(f"This Automodel will run all possible models for classification through MLJar automated Machine learning.")

            if st.button("Run AutoModel"):
                if target_feature == None:
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

        if  (target_feature is not None and model_choice is not None and mljar_task is False):
            if(st.button("Run Model")):
                if model_choice == "Logistic Regression":
                    classificationCodeTemplate.run_classification(dataset, target_feature, model_choice, f"🔐{model_choice}")

                elif model_choice == "K-Nearest Neighbors":
                    classificationCodeTemplate.run_classification(dataset, target_feature, model_choice, f"🔐{model_choice}")

                elif model_choice == "Support Vector Machine":
                    classificationCodeTemplate.run_classification(dataset, target_feature, model_choice, f"🔐{model_choice}")

                elif model_choice == "Naive Bayes":
                    classificationCodeTemplate.run_classification(dataset, target_feature, model_choice, f"🔐{model_choice}")

                elif model_choice == "Decision Tree Classifier":
                    classificationCodeTemplate.run_classification(dataset, target_feature, model_choice, f"🔐{model_choice}")

