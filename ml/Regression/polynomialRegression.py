import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from .regression_utils import preprocess_data, evaluate_model
import ml.Regression.regressionReport as regressionReport


def run_polynomial_regression(dataset, target_col, degree=2):
    st.subheader("📈 Polynomial Regression")

    X_train, X_test, y_train, y_test = preprocess_data(dataset, target_col)
    if X_train is None:
        return

    if X_train.shape[1] > 5:
        st.warning("Polynomial regression can overfit with too many features. Reduce dimensions.")
        return

    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    y_pred = model.predict(X_test)
    regressionReport.regression_report(y_test, y_pred)
    return y_test, y_pred