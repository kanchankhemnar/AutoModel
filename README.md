# 🔥 AutoModel — Version 1.0

AutoModel is a Firebase-powered AutoML Dashboard built using **Streamlit** that lets users upload, analyze, train, and download machine learning models — all from a beautiful web interface.

This is **Version 1.0**, focused on:

- ✅ Firebase Auth (Login/Signup)
- ✅ Uploading custom datasets
- ✅ Exploratory Data Profiling
- ✅ AutoML training via `mljar-supervised` and `ML models`
- ✅ Downloading trained models
- ✅ Modular backend structure for Firebase, ML, and Storage
- ✅ Deployed LIVE on Render

---

## 🚀 Live Demo

👉 [Visit AutoModel on Render](https://automodel.onrender.com)

---

## 🧠 Features

| Feature                  | Description                                                  |
|--------------------------|--------------------------------------------------------------|
| 🔐 Firebase Auth         | Email/password login using Pyrebase + Firebase Admin SDK     |
| 📤 Dataset Upload        | Upload your own `.csv` or select sample datasets             |
| 📊 Data Profiling        | Visual + statistical summaries of your dataset (via ydata)   |
| 🤖 AutoML Training       | Train classification & regression models via MLJar AutoML    |
| 📥 Model Download        | Download trained `.pkl` model files easily                   |
| ☁️ Firebase Integration  | Firestore + Firebase Storage for user data & file handling   |
| 💻 Modular Codebase      | Separated backend + frontend folders (Streamlit-monolith)    |

---

## 🗂 Project Structure
AutoModel/
├── app.py # Entry point (Streamlit)
├── frontend/ # UI logic: train, upload, etc.
├── backend/ # Firebase logic, ML models
│ ├── firestore/
│ ├── firebase/
│ ├── ml/
├── models/ # Firestore interaction files (datasets, models, reports)
├── SampleDatasets/ # (Migrating to Firebase Storage)
├── information/ # (Migrating to Firebase Storage)
├── requirements.txt
├── .python-version


---

## 🛠 Tech Stack

- 🧪 **Streamlit** — frontend UI
- 🔐 **Firebase** — Auth, Firestore, Storage
- 📦 **Pyrebase4** + `firebase-admin`
- 🤖 **mljar-supervised** — AutoML core engine
- 🧠 `scikit-learn`, `seaborn`, `pandas`, `matplotlib`
- ☁️ **Render** — hosting + deployment

---

## 🔧 Setup Locally

```bash
git clone https://github.com/kanchankhemnar/AutoModel.git
cd AutoModel

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Add Firebase config in secrets.toml or .env

# Run app
streamlit run app.py
