import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, root_mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.exceptions import NotFittedError
import streamlit as st

def preprocess_data(df, target):
        if(target=="Select"):
            st.warning("Please select a target column to continue.")
            return None, None, None, None
        if df.isnull().sum().sum() > 0:
            st.warning("⚠️ Dataset contains missing values. Please clean your data.")
            return None, None, None, None

        X = df.drop(columns=[target])
        y = df[target]

        if X.select_dtypes(include=['object', 'category']).shape[1] > 0:
            X = pd.get_dummies(X)

        try:
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)
        except Exception as e:
            st.error(f"Scaling error: {str(e)}")
            return None, None, None, None

        return train_test_split(X_scaled, y, test_size=0.2, random_state=42)

def evaluate_model(model, X_test, y_test):
        try:
            y_pred = model.predict(X_test)
        except NotFittedError:
            st.error("Model could not be trained.")
            return

    # st.success("✅ Model Trained Successfully!")
    # st.markdown("### 📊 Evaluation Metrics")
    # st.write(f"R² Score: {r2_score(y_test, y_pred):.4f}")
    # st.write(f"RMSE: {root_mean_squared_error(y_test, y_pred):.4f}")
    # st.write(f"MAE: {mean_absolute_error(y_test, y_pred):.4f}")
