# 🏥 MediPredict Pro - AI Multi Disease Prediction System

A complete, production-ready AI Multi Disease Prediction web application built with **Python**, **Streamlit**, and **Scikit-Learn**. The system features pre-trained machine learning models for **Diabetes**, **Heart Disease**, and **Parkinson's Disease**, featuring automated feature generation, clinical validation, sample patient presets, and commercial medical UI aesthetics.

---

## 🌟 Key Features

- **Professional Medical UI/UX**: Designed with a clean Blue + White + Light Green medical palette, glassmorphism, responsive cards, smooth transitions, and custom CSS.
- **Three Specialized Prediction Modules**:
  1. 🩸 **Diabetes Prediction**: 8 clinical parameters (Pima Indian Dataset) using pre-trained Linear Support Vector Machine (SVM).
  2. ❤️ **Heart Disease Prediction**: 13 cardiovascular indicators (UCI Heart Dataset) using pre-trained Logistic Regression.
  3. 🧠 **Parkinson's Disease Prediction**: 22 biomedical voice acoustic features (Oxford Voice Dataset) using pre-trained Support Vector Classifier (SVC).
- **1-Click Sample Patient Presets**: Instantly load pre-configured high-risk or healthy subject profiles to test model inferences without manual typing.
- **Inference & Confidence Scoring**: Displays AI diagnosis classification with confidence probability calculations.
- **Dataset Analytics Dashboard**: Built-in dataset inspection tool with statistical summaries, correlation matrices, and distribution graphs.
- **Input Validation & Medical Tooltips**: Tooltips and physiological boundary validation for every feature parameter.

---

## 📂 Project Structure

```
📂 multi_disease_app/
│── app.py                   # Main Streamlit entrypoint & router
│── requirements.txt         # Project Python dependencies
│── README.md                # Documentation & setup guide
│── models/                  # Pre-trained ML model binaries (.sav)
│   ├── diabetes_model.sav
│   ├── heart_disease_model.sav
│   └── parkinsons_model.sav
│── datasets/                # Original datasets
│   ├── diabetes.csv
│   ├── heart.csv
│   └── parkinsons.csv
│── assets/                  # Custom CSS design system
│   └── style.css
│── utils/                   # Utilities & helper modules
│   ├── model_loader.py      # Cached model loader & inference engine
│   ├── feature_metadata.py  # Feature metadata, ranges, tooltips & presets
│   └── ui_components.py     # Custom UI cards, hero banners, results & alerts
└── pages_view/              # Application Page Views
    ├── home.py              # Home Dashboard
    ├── diabetes.py          # Diabetes Prediction View
    ├── heart.py             # Heart Disease Prediction View
    ├── parkinsons.py        # Parkinson's Prediction View
    ├── analytics.py         # Clinical Data Analytics
    └── about.py             # About & Medical Disclaimer
```

---

## 🚀 Quick Start Guide

### 1. Requirements
Ensure Python 3.9+ (or Anaconda Python) is installed.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch Application
```bash
streamlit run app.py
```

The application will launch in your browser at `http://localhost:8501`.

---

## 🔒 Security & Medical Disclaimer

This application is intended strictly for educational, research, and informational reference. It does not replace professional medical advice, clinical diagnosis, or medical treatment.
