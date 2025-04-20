import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    classification_report, confusion_matrix, ConfusionMatrixDisplay
)
from utils.save_outputs import save_plot, save_html_report
import streamlit as st
import time

def generate_classification_report(y_true, y_pred):
    with st.spinner("Executing..."):
        time.sleep(3)
    st.markdown("## 🧾 Classification Report")

    # Metrics
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, average="weighted")
    rec = recall_score(y_true, y_pred, average="weighted")
    f1 = f1_score(y_true, y_pred, average="weighted")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Accuracy", f"{acc:.4f}",border=True)
    col2.metric("Precision", f"{prec:.4f}",border=True)
    col3.metric("Recall", f"{rec:.4f}",border=True)
    col4.metric("F1 Score", f"{f1:.4f}",border=True)

    # Confusion Matrix
    cm = confusion_matrix(y_true, y_pred)
    fig, ax = plt.subplots(figsize=(8, 2))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
    ax.set_title("Confusion Matrix",fontsize=7)
    ax.set_xlabel("Predicted",fontsize=7)
    ax.set_ylabel("Actual",fontsize=7)
    ax.tick_params(axis='both', labelsize=4)
    st.pyplot(fig)

    # Save plot
    save_plot(fig, "confusion_matrix.png")

    # Classification Report HTML
    report = classification_report(y_true, y_pred)
    
    save_html_report(f"<pre>{report}</pre>", "classification_report.html")
