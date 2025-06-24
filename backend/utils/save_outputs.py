import os
import joblib

def save_model(model, filename="trained_model.pkl"):
    os.makedirs("artifacts", exist_ok=True)
    joblib.dump(model, f"artifacts/{filename}")

def save_plot(fig, filename):
    os.makedirs("artifacts", exist_ok=True)
    fig.savefig(f"artifacts/{filename}", bbox_inches="tight")

def save_html_report(html_content, filename="regression_report.html"):
    os.makedirs("artifacts", exist_ok=True)
    with open(f"artifacts/{filename}", "w", encoding="utf-8") as f:
        f.write(html_content)
