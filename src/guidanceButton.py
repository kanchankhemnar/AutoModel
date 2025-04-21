import streamlit as st
import os

def get_info_filename(model_choice, inner_model_choice):
    if model_choice is None:
        return "mlTasks.txt"
    elif model_choice == "Classification":
        if inner_model_choice == "Binary Classification":
            return "classification/binaryClassification.txt"
        
        elif inner_model_choice == "Multiclass Classification":
            return "classification/multiclassClassification.txt"
        
        elif inner_model_choice == "Logistic Regression":
            return "classification/logisticRegression.txt"
        
        elif inner_model_choice == "K-Nearest Neighbors":
            return "classification/knn.txt"
        
        elif inner_model_choice == "Support Vector Machine":
            return "classification/svm.txt"
        
        elif inner_model_choice == "Naive Bayes":
            return "classification/naiveBayes.txt"
        
        elif inner_model_choice == "Decision Tree Classifier":
            return "classification/decisionTreeClassifier.txt"
        
        else:
            return "classification/classification.txt"
    elif model_choice == "Regression":

        if inner_model_choice == "Linear Regression":
            return "regression/linearRegression.txt"
        
        elif inner_model_choice == "Multiple Regression":
            return "regression/multipleRegression.txt"
        
        elif inner_model_choice == "Random Forest Regression":
            return "regression/randomForestRegression.txt"
        
        elif inner_model_choice == "Decision Tree Regression":
            return "regression/decisionTreeRegression.txt"
        
        elif inner_model_choice == "Polynomial Regression":
            return "regression/polynomialRegression.txt"
        
        else:
            return "regression/regression.txt"
        
    return "mlTasks.txt"

def show_info_popup(filename):
    path = os.path.join("information", filename)
    if os.path.exists(path):
        with open(path, "r") as file:
            content = file.read()
        with st.expander("📘 Read More"):
            st.markdown(content)
    else:
        st.warning("Information not available.")

def render_info_button(model_choice, inner_model_choice):
    filename = get_info_filename(model_choice, inner_model_choice)
    label_map = {
        "mlTasks.txt": "Read about ML Tasks",
        "classification/classification.txt": "Read about Classification",
        "classification/binaryClassification.txt": "Read about Binary Classification",
        "classification/multiclassClassification.txt": "Read about Multiclass Classification",
        "classification/decisionTreeClassifier.txt": "Read about Decision Tree Classification",
        "classification/knn.txt": "Read about K-Nearest Neighbors",
        "classification/svm.txt": "Read about Support Vector Machine",
        "classification/logisticRegression.txt": "Read about Logistic Regression",
        "classification/naiveBayes.txt": "Read about Naive Bayes",
        "regression/regression.txt": "Read about Regression",
        "regression/linearRegression.txt": "Read about Linear Regression",
        "regression/multipleRegression.txt": "Read about Multiple Regression",
        "regression/decisionTreeRegression.txt": "Read about Decision Tree Regression",
        "regression/randomForestRegression.txt": "Read about Random Forest",
        "regression/polynomialRegression.txt": "Read about Polynomial Regression",

    }
    button_label = label_map.get(filename, "Read Info")

    if st.button(f"📘 {button_label}", use_container_width=True):
        show_info_popup(filename)
