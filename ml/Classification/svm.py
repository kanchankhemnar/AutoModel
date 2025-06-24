from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from ml.Classification import classificationReport
from backend.utils.save_outputs import save_model
import pandas as pd
import streamlit as st

def run_svm(dataset, target_col):
    st.subheader("🔐 Support Vector Machine")

    X = dataset.drop(columns=[target_col])
    y = dataset[target_col]

    # Basic preprocessing
    X = pd.get_dummies(X)  # encode categoricals
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = SVC()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Save model
    save_model(model)

    # Show + Save report
    classificationReport.generate_classification_report(y_test, y_pred)
    return y_test, y_pred