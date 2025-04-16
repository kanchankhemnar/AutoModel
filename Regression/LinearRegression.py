from sklearn.linear_model import LinearRegression
import streamlit as st
from .regression_utils import preprocess_data, evaluate_model
import Regression.regressionReport as regressionReport


def run_linear_regression(dataset, target_col):
    st.subheader("📈 Linear Regression")

    X_train, X_test, y_train, y_test = preprocess_data(dataset, target_col)
    if X_train is None:
        return

    if len(X_train[0]) > 1:
        st.warning("Linear Regression assumes single feature. For multiple, use Multiple Regression.")
        return

    model = LinearRegression()
    model.fit(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    y_pred = model.predict(X_test)
    regressionReport.regression_report(y_test, y_pred)