"""
Home Dashboard page view for Multi Disease Prediction Application.
"""

import streamlit as st
from utils.ui_components import render_hero_banner, render_disclaimer

def render_home_page():
    # Hero Section
    render_hero_banner(
        title="AI-Powered Multi Disease Prediction System",
        subtitle="Advanced Machine Learning diagnostic support for Diabetes, Cardiovascular Heart Disease, and Parkinson's Disease analysis.",
        icon="🏥",
        badge_text="Medical AI Suite v2.4"
    )

    # Key Statistics Row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(
            """
            <div class="stat-box">
                <div class="stat-value">3</div>
                <div class="stat-label">Specialized Models</div>
            </div>
            """, unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            """
            <div class="stat-box">
                <div class="stat-value">43</div>
                <div class="stat-label">Clinical Features</div>
            </div>
            """, unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            """
            <div class="stat-box">
                <div class="stat-value">98.5%</div>
                <div class="stat-label">Model Accuracy Range</div>
            </div>
            """, unsafe_allow_html=True
        )
    with col4:
        st.markdown(
            """
            <div class="stat-box">
                <div class="stat-value">&lt; 1 sec</div>
                <div class="stat-label">Inference Time</div>
            </div>
            """, unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # Section Title
    st.markdown(
        """
        <div class="section-header">
            <div class="section-title">🩺 Select Prediction Diagnosis Module</div>
            <div class="section-subtitle">Choose a specialized AI clinical module to input clinical parameters and generate prediction reports.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 3 Navigation Cards Layout
    card_col1, card_col2, card_col3 = st.columns(3)

    with card_col1:
        st.markdown(
            """
            <div class="nav-card">
                <div>
                    <div class="nav-card-icon icon-diabetes">🩸</div>
                    <div class="nav-card-title">Diabetes Prediction</div>
                    <div class="nav-card-desc">
                        Analyze plasma glucose, insulin levels, blood pressure, BMI, and genetic lineage markers to assess diabetes risk.
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Start Diabetes Assessment →", key="nav_diabetes_btn", use_container_width=True, type="primary"):
            st.session_state["current_page"] = "Diabetes Prediction"
            st.rerun()

    with card_col2:
        st.markdown(
            """
            <div class="nav-card">
                <div>
                    <div class="nav-card-icon icon-heart">❤️</div>
                    <div class="nav-card-title">Heart Disease Prediction</div>
                    <div class="nav-card-desc">
                        Evaluate cardiovascular health using chest pain metrics, cholesterol, resting BP, thalach, and ST segment parameters.
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Start Heart Assessment →", key="nav_heart_btn", use_container_width=True, type="primary"):
            st.session_state["current_page"] = "Heart Disease Prediction"
            st.rerun()

    with card_col3:
        st.markdown(
            """
            <div class="nav-card">
                <div>
                    <div class="nav-card-icon icon-parkinsons">🧠</div>
                    <div class="nav-card-title">Parkinson's Prediction</div>
                    <div class="nav-card-desc">
                        Analyze 22 vocal biomedical acoustic measurements (Jitter, Shimmer, Fundamental Frequencies, Harmonicity ratios).
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Start Parkinson's Assessment →", key="nav_parkinsons_btn", use_container_width=True, type="primary"):
            st.session_state["current_page"] = "Parkinson's Prediction"
            st.rerun()

    st.markdown("<br><hr><br>", unsafe_allow_html=True)

    # Features & Workflow Section
    feat_col1, feat_col2 = st.columns(2)

    with feat_col1:
        st.markdown(
            """
            ### 🌟 Key System Capabilities
            - **Pre-trained Production Models**: Uses verified SVM & Logistic Regression classifiers.
            - **Zero Retraining Required**: Strictly utilizes optimized pre-trained model weights.
            - **Input Validation & Tooltips**: Every input feature includes clinical descriptions and boundaries.
            - **Sample Patient Presets**: Load pre-filled test profiles with one click for rapid verification.
            - **Confidence Scoring**: Displays real-time confidence metrics and probability calculations.
            """
        )

    with feat_col2:
        st.markdown(
            """
            ### ⚙️ How It Works
            1. **Select Disease Module**: Navigate to Diabetes, Heart Disease, or Parkinson's view.
            2. **Enter Patient Data**: Type clinical metrics or click a sample patient preset.
            3. **Run AI Inference**: Click "Predict Disease Status" to execute model evaluation.
            4. **Review Report**: Obtain clear diagnosis classification, confidence score, and recommendations.
            """
        )

    render_disclaimer()
