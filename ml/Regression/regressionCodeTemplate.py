def run_regression(dataset, target_col, model_choice, header):
    from sklearn.tree import DecisionTreeRegressor
    import streamlit as st
    from .regression_utils import preprocess_data
    import ml.Regression.regressionReport as regressionReport
    st.subheader(header)

    X_train, X_test, y_train, y_test = preprocess_data(dataset, target_col)
    if X_train is None:
        return
    
    algorithm = None

    if model_choice == "Linear Regression":
      if len(X_train[0]) > 1:
        st.warning("Linear Regression assumes single feature. For multiple features, use Multiple Regression.")
        return
      from sklearn.linear_model import LinearRegression
      algorithm = LinearRegression()


    elif model_choice == "Multiple Regression":
      if X_train.shape[1] <= 1:
          st.warning("Multiple Regression requires more than one feature. Use Linear Regression instead.")
          return
      from sklearn.linear_model import LinearRegression
      algorithm = LinearRegression()

    elif model_choice == "Polynomial Regression":
      if X_train.shape[1] > 5:
        st.warning("Polynomial regression can overfit with too many features. Reduce dimensions.")
        return
      from sklearn.linear_model import LinearRegression
      from sklearn.preprocessing import PolynomialFeatures
      from sklearn.pipeline import make_pipeline

      algorithm = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())

    elif model_choice == "Random Forest Regression":
      from sklearn.ensemble import RandomForestRegressor
      algorithm = RandomForestRegressor()

    elif model_choice == "Decision Tree Regression":
      from sklearn.tree import DecisionTreeRegressor
      algorithm = DecisionTreeRegressor()

    if algorithm is not None :
      model = algorithm
      model.fit(X_train, y_train)
      from sklearn.exceptions import NotFittedError    
      try:
          y_pred = model.predict(X_test)
          regressionReport.regression_report(y_test, y_pred)
          return y_test, y_pred
      except NotFittedError:
          st.error("Model could not be trained.")
          return  
    return