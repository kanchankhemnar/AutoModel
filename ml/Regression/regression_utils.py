import streamlit as st
def preprocess_data(df, target):
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
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


