from sklearn.linear_model import LinearRegression
import streamlit as st
from .regression_utils import preprocess_data, evaluate_model
import ml.Regression.regressionReport as regressionReport

def run_multiple_regression(dataset, target_col):
    st.subheader("📈 Multiple Linear Regression")

    X_train, X_test, y_train, y_test = preprocess_data(dataset, target_col)
    if X_train is None:
        return

    model = LinearRegression()
    model.fit(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    y_pred = model.predict(X_test)
    regressionReport.regression_report(y_test, y_pred)
    return y_test, y_pred 
