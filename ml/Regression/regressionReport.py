import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score, root_mean_squared_error, mean_absolute_error
import numpy as np
import time
from backend.utils.save_outputs import save_html_report,save_plot



def regression_report(y_true, y_pred):
    with st.spinner("Executing 🚀..."):
        time.sleep(3)
    st.markdown("## 📊 Model Evaluation Report")

    # Metrics
    r2 = r2_score(y_true, y_pred)
    rmse = root_mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)

    col1, col2, col3 = st.columns(3)
    col1.metric("R² Score", f"{r2:.3f}",border=True)
    col2.metric("RMSE", f"{rmse:.3f}",border=True)
    col3.metric("MAE", f"{mae:.3f}",border=True)

    # Visuals
    st.markdown("### 🔍 Residuals vs Predicted")
    fig1, ax1 = plt.subplots(figsize=(5,2))
    residuals = y_true - y_pred
    sns.scatterplot(x=y_pred, y=residuals, ax=ax1,s=15)
    ax1.axhline(0, color='red', linestyle='--')
    ax1.tick_params(axis='both', labelsize=6)
    ax1.set_xlabel("Predicted Values",fontsize=6)
    ax1.set_ylabel("Residuals",fontsize=6)
    st.pyplot(fig1)

    st.markdown("### 🎯 Actual vs Predicted")
    fig2, ax2 = plt.subplots(figsize=(5,2))
    sns.scatterplot(x=y_true, y=y_pred, ax=ax2)
    ax2.plot([min(y_true), max(y_true)], [min(y_true), max(y_true)], 'r--')
    ax2.tick_params(axis='both', labelsize=6)
    ax2.set_xlabel("Actual Values",fontsize=6)
    ax2.set_ylabel("Predicted Values",fontsize=6)
    st.pyplot(fig2)

    st.markdown("### 📦 Error Distribution")
    fig3, ax3 = plt.subplots(figsize=(5,2))
    sns.histplot(y_true - y_pred, kde=True, ax=ax3, color="purple")
    ax3.tick_params(axis='both', labelsize=6)
    ax3.set_xlabel("Error",fontsize=6)
    st.pyplot(fig3)

    st.markdown("### 📉 Error Boxplot")
    fig4, ax4 = plt.subplots(figsize=(8,3))
    sns.boxplot(x=y_true - y_pred, ax=ax4)
    ax4.tick_params(axis='both', labelsize=6)
    ax4.set_xlabel("Prediction Error",fontsize=6)
    st.pyplot(fig4)

    # saving images 
    
    save_plot(fig1, "residuals_plot.png")
    save_plot(fig2, "actual_vs_pred.png")
    save_plot(fig3, "error_dist.png")
    save_plot(fig4, "error_boxplot.png")

    # Saving HTML report
    html_content = f"""
    <html>
    <head><title>Regression Report</title></head>
    <body>
    <h2>📊 Model Metrics</h2>
    <p><b>R² Score:</b> {r2:.4f}</p>
    <p><b>RMSE:</b> {rmse:.4f}</p>
    <p><b>MAE:</b> {mae:.4f}</p>
    </body>
    </html>
    """
    save_html_report(html_content)