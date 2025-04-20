import streamlit as st
import os

def download_models():
    st.title("📥 Download Center")
    st.markdown("Here you can download your trained model, reports, and evaluation plots.")

    if not os.path.exists("artifacts"):
        st.warning("🚫 No files available yet. Train a model first.")
        return

    # Download model
    model_path = "artifacts/trained_model.pkl"
    if os.path.exists(model_path):
        with open(model_path, "rb") as f:
            st.download_button("🤖 Download Trained Model", f, file_name="trained_model.pkl")

    # Download HTML report
    report_path = "artifacts/regression_report.html"
    if os.path.exists(report_path):
        with open(report_path, "rb") as f:
            st.download_button("📄 Download Report (HTML)", f, file_name="regression_report.html")

    # Download Residual Plot
    residual_plot_path = "artifacts/residuals_plot.png"
    if os.path.exists(residual_plot_path):
        with open(residual_plot_path, "rb") as f:
            st.download_button("📊 Download Residual Plot", f, file_name="residuals_plot.png")

    # Add more plots as needed
    # ...

    st.markdown("---")
    st.info("📝 If you don't see any downloads, please run the model training step first.")
