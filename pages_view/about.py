"""
About & Medical Disclaimer Page View.
"""

import streamlit as st
from utils.ui_components import render_hero_banner, render_disclaimer

def render_about_page():
    render_hero_banner(
        title="About MediPredict Pro AI",
        subtitle="A commercial-grade clinical decision support application powered by machine learning.",
        icon="ℹ️",
        badge_text="System Information"
    )

    st.markdown(
        """
        ### 🏥 Project Mission & Architecture
        **MediPredict Pro** provides rapid, reproducible, and explainable artificial intelligence prediction models for three critical clinical domains:
        1. **Diabetes Mellitus (Pima Indian Dataset)**: Support Vector Machine (SVM) kernel linear classifier analyzing metabolic & genetic markers.
        2. **Cardiovascular Heart Disease (UCI Heart Dataset)**: Logistic Regression classifier evaluating blood pressure, cholesterol, resting ECG, and stress test metrics.
        3. **Parkinson's Disease (Oxford Voice Dataset)**: Support Vector Machine (SVM) analyzing 22 vocal biomedical acoustic measurements.

        ---

        ### 🛡️ Production & Security Guarantee
        - **No Model Retraining**: Strictly utilizes verified pre-trained binaries.
        - **Data Privacy**: No patient medical records are stored or transmitted externally.
        - **Input Validation**: All parameters undergo boundary checks to ensure physiological consistency.

        ---

        ### 📧 Contact & Support
        For inquiries regarding deployment, clinical model integration, or technical support:
        - **System Developer**: AI Healthcare Engineering Team
        - **Framework**: Python 3.12, Streamlit, Scikit-Learn
        - **Application Version**: 2.4.0 (Commercial Build)
        """
    )

    render_disclaimer()
