from sklearn.tree import DecisionTreeRegressor
import streamlit as st
from .regression_utils import preprocess_data, evaluate_model
import Regression.regressionReport as regressionReport

def run_decision_tree(dataset, target_col):
    st.subheader("🌳 Decision Tree Regression")

    X_train, X_test, y_train, y_test = preprocess_data(dataset, target_col)
    if X_train is None:
        return

    model = DecisionTreeRegressor()
    model.fit(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    y_pred = model.predict(X_test)
    regressionReport.regression_report(y_test, y_pred)
    return y_test, y_pred