from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from Classification import classificationReport
from utils.save_outputs import save_model
import pandas as pd
import streamlit as st

def run_knn(dataset, target_col):
    st.subheader("🔐 K-Nearest Neighbors")

    X = dataset.drop(columns=[target_col])
    y = dataset[target_col]

    # Basic preprocessing
    X = pd.get_dummies(X)  # encode categoricals
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = KNeighborsClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Save model
    save_model(model)

    # Show + Save report
    classificationReport.generate_classification_report(y_test, y_pred)
