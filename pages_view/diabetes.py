"""
Diabetes Prediction Page View.
"""

import streamlit as st
import time
from utils.feature_metadata import DIABETES_METADATA, DIABETES_PRESETS
from utils.model_loader import predict_disease
from utils.ui_components import render_hero_banner, render_prediction_result, render_disclaimer

def render_diabetes_page():
    render_hero_banner(
        title="Diabetes Prediction Module",
        subtitle="Clinical analysis based on 8 diagnostic parameters from the Pima Indian Diabetes dataset using Support Vector Machine (SVM) Classification.",
        icon="🩸",
        badge_text="SVM Model Loaded"
    )

    st.markdown("### 📋 Patient Clinical Parameters")
    st.info("Enter patient clinical test results below or load a preset test profile.")

    # Preset Selection Buttons
    preset_cols = st.columns([1, 1, 2])
    with preset_cols[0]:
        if st.button("💉 Load Diabetic Sample", type="secondary", use_container_width=True):
            st.session_state["diabetes_data"] = DIABETES_PRESETS["Diabetic Female Patient"].copy()
            st.toast("Loaded Diabetic Patient Profile!", icon="📋")
    with preset_cols[1]:
        if st.button("🌱 Load Healthy Sample", type="secondary", use_container_width=True):
            st.session_state["diabetes_data"] = DIABETES_PRESETS["Healthy Female Patient"].copy()
            st.toast("Loaded Healthy Patient Profile!", icon="✅")
    with preset_cols[2]:
        if st.button("🔄 Reset All Inputs", use_container_width=True):
            st.session_state["diabetes_data"] = {k: v["default"] for k, v in DIABETES_METADATA.items()}
            st.session_state.pop("diabetes_prediction_result", None)
            st.toast("Reset all fields to default values.", icon="🔄")

    # Initialize Session State if not present
    if "diabetes_data" not in st.session_state:
        st.session_state["diabetes_data"] = {k: v["default"] for k, v in DIABETES_METADATA.items()}

    # Input Form Layout
    with st.form("diabetes_form"):
        col1, col2 = st.columns(2)
        
        form_values = {}
        features = list(DIABETES_METADATA.keys())

        for i, feat_key in enumerate(features):
            meta = DIABETES_METADATA[feat_key]
            current_val = st.session_state["diabetes_data"].get(feat_key, meta["default"])
            
            target_col = col1 if i % 2 == 0 else col2
            
            with target_col:
                if isinstance(meta["default"], float):
                    val = st.number_input(
                        label=f"{meta['label']} ({meta['unit']})",
                        min_value=float(meta["min"]),
                        max_value=float(meta["max"]),
                        value=float(current_val),
                        step=float(meta["step"]),
                        help=meta["tooltip"],
                        key=f"input_diab_{feat_key}"
                    )
                else:
                    val = st.number_input(
                        label=f"{meta['label']} ({meta['unit']})",
                        min_value=int(meta["min"]),
                        max_value=int(meta["max"]),
                        value=int(current_val),
                        step=int(meta["step"]),
                        help=meta["tooltip"],
                        key=f"input_diab_{feat_key}"
                    )
                form_values[feat_key] = val

        st.markdown("<br>", unsafe_allow_html=True)
        submit_btn = st.form_submit_button("🔍 Predict Diabetes Risk Status", type="primary", use_container_width=True)

    # Perform Prediction
    if submit_btn:
        # Save current form values into session state
        st.session_state["diabetes_data"] = form_values.copy()
        
        # Validation checks
        warnings = []
        if form_values["Glucose"] == 0:
            warnings.append("Plasma Glucose concentration is set to 0 mg/dL (physiologically unusual).")
        if form_values["BloodPressure"] == 0:
            warnings.append("Blood Pressure is set to 0 mm Hg.")

        for w in warnings:
            st.warning(f"⚠️ Validation Warning: {w}")

        with st.spinner("⚡ Running SVM Model Analysis..."):
            time.sleep(0.4)
            # Input values in exact feature order:
            # Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age
            feature_array = [form_values[k] for k in features]
            result = predict_disease("diabetes", feature_array)
            st.session_state["diabetes_prediction_result"] = result

    # Display Prediction Result if available
    if "diabetes_prediction_result" in st.session_state:
        st.markdown("<br>", unsafe_allow_html=True)
        render_prediction_result(st.session_state["diabetes_prediction_result"], "Diabetes")

    render_disclaimer()
