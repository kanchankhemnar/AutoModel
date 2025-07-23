def run_classification(dataset, target_col, classificationAlgo, header):
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from ml.Classification import classificationReport
    from backend.utils.save_outputs import save_model
    import pandas as pd
    import streamlit as st

    algorithm = None

    st.subheader(header)

    X = dataset.drop(columns=[target_col])
    y = dataset[target_col]

    # Basic preprocessing
    X = pd.get_dummies(X)  # encode categoricals
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    if(classificationAlgo == "Logistic Regression"):
        from sklearn.linear_model import LogisticRegression
        algorithm = LogisticRegression()
    
    if(classificationAlgo == "K-Nearest Neighbors"):
        from sklearn.neighbors import KNeighborsClassifier
        algorithm = KNeighborsClassifier()

    if(classificationAlgo == "Support Vector Machine"):
        from sklearn.svm import SVC
        algorithm = SVC()

    if(classificationAlgo == "Naive Bayes"):
        from sklearn.naive_bayes import GaussianNB
        algorithm = GaussianNB()

    if(classificationAlgo == "Decision Tree Classifier"):
        from sklearn.tree import DecisionTreeClassifier
        algorithm = DecisionTreeClassifier()

    model = algorithm
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Save model
    save_model(model)

    # Show + Save report
    classificationReport.generate_classification_report(y_test, y_pred)
    return y_test, y_pred