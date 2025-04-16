import streamlit as st
from supervised.automl import AutoML
import streamlit.components.v1 as component
from Regression import linearRegression, multipleRegression, polynomialRegression, randomForest, decisionTreeRegression

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

                    automl = AutoML(
                        mode="Compete",
                        ml_task="regression",
                        total_time_limit=60,
                        results_path="automl_results",
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
