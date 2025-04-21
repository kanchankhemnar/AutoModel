# import streamlit as st
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd
# from sklearn.metrics import r2_score, accuracy_score
# from Regression import linearRegression, decisionTreeRegression, randomForest, multipleRegression, polynomialRegression
# from Classification import knn, logisticRegression, naiveBayes, decisionTree, svm


# def run_model_and_get_metric(task_type, model_name, dataset, target_feature):
#     if task_type == "Regression":
#         if model_name == "Linear Regression":
#             y_test, y_pred = linearRegression.run_linear_regression(dataset, target_feature)
#             return r2_score(y_test, y_pred)
#         elif model_name == "Decision Tree Regression":
#             y_test, y_pred = decisionTreeRegression.run_decision_tree(dataset, target_feature)
#             return r2_score(y_test, y_pred)
#         elif model_name == "Random Forest Regression":
#             y_test, y_pred = randomForest.run_random_forest(dataset, target_feature)
#             return r2_score(y_test, y_pred)

#     elif task_type == "Classification":
#         if model_name == "Logistic Regression":
#             y_test, y_pred = logisticRegression.run_logistic_regression(dataset, target_feature)
#             return accuracy_score(y_test, y_pred)
#         elif model_name == "Decision Tree Classifier":
#             y_test, y_pred = decisionTree.run_decision_tree(dataset, target_feature)
#             return accuracy_score(y_test, y_pred)
#         elif model_name == "Random Forest Classifier":
#             y_test, y_pred = randomForest.run_random_forest(dataset, target_feature)
#             return accuracy_score(y_test, y_pred)
#         elif model_name == "Naive Bayes":
#             y_test, y_pred = naiveBayes.run_naive_bayes(dataset, target_feature)
#             return accuracy_score(y_test, y_pred)
#         elif model_name == "K-Nearest Neighbors":
#             y_test, y_pred = knn.run_knn(dataset, target_feature)
#             return accuracy_score(y_test, y_pred)
#         elif model_name == "Support Vector Machine":
#             y_test, y_pred = svm.run_svm(dataset, target_feature)
#             return accuracy_score(y_test, y_pred)

#     return None


# def render_model_comparison(dataset, target_feature, task_type):
#     st.markdown("## :bar_chart: Compare Model Performance")

#     if task_type == "Regression":
#         available_models = [
#             "Linear Regression",
#             "Decision Tree Regression",
#             "Random Forest Regression"
#         ]
#     else:
#         available_models = [
#             "Logistic Regression",
#             "Decision Tree Classifier",
#             "Random Forest Classifier",
#             "Naive Bayes",
#             "K-Nearest Neighbors",
#             "Support Vector Machine"
#         ]

#     selected_models = st.multiselect("Select models to compare", available_models)

#     if selected_models and st.button("Compare Selected Models"):
#         results = {}
#         for model in selected_models:
#             score = run_model_and_get_metric(task_type, model, dataset, target_feature)
#             results[model] = round(score, 4) if score is not None else 0

#         # Plotting
#         fig, ax = plt.subplots()
#         sns.barplot(x=list(results.values()), y=list(results.keys()), palette="Blues_d", ax=ax)
#         ax.set_xlabel("Accuracy" if task_type == "Classification" else "R² Score")
#         ax.set_title("Model Comparison")
#         st.pyplot(fig)

#         st.write(pd.DataFrame.from_dict(results, orient='index', columns=["Score"]))