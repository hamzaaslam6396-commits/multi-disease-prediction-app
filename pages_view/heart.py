"""
Heart Disease Prediction Page View.
"""

import streamlit as st
import time
from utils.feature_metadata import HEART_METADATA, HEART_PRESETS
from utils.model_loader import predict_disease
from utils.ui_components import render_hero_banner, render_prediction_result, render_disclaimer

def render_heart_page():
    render_hero_banner(
        title="Heart Disease Prediction Module",
        subtitle="Cardiovascular risk assessment based on 13 clinical parameters using Logistic Regression classification.",
        icon="❤️",
        badge_text="Logistic Regression Model"
    )

    st.markdown("### 📋 Patient Cardiovascular Parameters")
    st.info("Fill in the patient's cardiovascular lab & physical examination metrics below or load a preset sample.")

    # Presets & Reset Row
    preset_cols = st.columns([1, 1, 2])
    with preset_cols[0]:
        if st.button("💔 Load High Risk Patient", type="secondary", use_container_width=True):
            st.session_state["heart_data"] = HEART_PRESETS["High Risk Patient Profile"].copy()
            st.toast("Loaded High Risk Heart Patient Profile!", icon="⚠️")
    with preset_cols[1]:
        if st.button("🌱 Load Healthy Patient", type="secondary", use_container_width=True):
            st.session_state["heart_data"] = HEART_PRESETS["Healthy Patient Profile"].copy()
            st.toast("Loaded Healthy Patient Profile!", icon="✅")
    with preset_cols[2]:
        if st.button("🔄 Reset All Inputs", use_container_width=True):
            st.session_state["heart_data"] = {
                k: (v["default"] if "default" in v else list(v["options"].keys())[0])
                for k, v in HEART_METADATA.items()
            }
            st.session_state.pop("heart_prediction_result", None)
            st.toast("Reset all fields to default values.", icon="🔄")

    # Initialize Session State
    if "heart_data" not in st.session_state:
        st.session_state["heart_data"] = {
            k: (v["default"] if "default" in v else list(v["options"].keys())[0])
            for k, v in HEART_METADATA.items()
        }

    # Form Layout
    with st.form("heart_form"):
        col1, col2 = st.columns(2)
        
        form_values = {}
        features = list(HEART_METADATA.keys())

        for i, feat_key in enumerate(features):
            meta = HEART_METADATA[feat_key]
            current_val = st.session_state["heart_data"].get(feat_key, meta.get("default", 0))
            
            target_col = col1 if i % 2 == 0 else col2
            
            with target_col:
                if "options" in meta:
                    # Categorical dropdown selection
                    options_dict = meta["options"]
                    # Find matching label for current numeric key
                    selected_key = st.selectbox(
                        label=f"{meta['label']}",
                        options=list(options_dict.keys()),
                        format_func=lambda x: options_dict[x],
                        index=list(options_dict.keys()).index(current_val) if current_val in options_dict else 0,
                        help=meta["tooltip"],
                        key=f"input_heart_{feat_key}"
                    )
                    form_values[feat_key] = selected_key
                elif isinstance(meta["default"], float):
                    val = st.number_input(
                        label=f"{meta['label']} ({meta['unit']})",
                        min_value=float(meta["min"]),
                        max_value=float(meta["max"]),
                        value=float(current_val),
                        step=float(meta["step"]),
                        help=meta["tooltip"],
                        key=f"input_heart_{feat_key}"
                    )
                    form_values[feat_key] = val
                else:
                    val = st.number_input(
                        label=f"{meta['label']} ({meta['unit']})",
                        min_value=int(meta["min"]),
                        max_value=int(meta["max"]),
                        value=int(current_val),
                        step=int(meta["step"]),
                        help=meta["tooltip"],
                        key=f"input_heart_{feat_key}"
                    )
                    form_values[feat_key] = val

        st.markdown("<br>", unsafe_allow_html=True)
        submit_btn = st.form_submit_button("🔍 Predict Cardiovascular Risk Status", type="primary", use_container_width=True)

    # Perform Prediction
    if submit_btn:
        st.session_state["heart_data"] = form_values.copy()
        
        # Validation warning check
        warnings = []
        if form_values["chol"] > 300:
            warnings.append("Serum Cholesterol level is exceptionally high (> 300 mg/dL).")
        if form_values["trestbps"] > 160:
            warnings.append("Resting blood pressure indicates Stage 2 Hypertension (> 160 mm Hg).")

        for w in warnings:
            st.warning(f"⚠️ Clinical Flag: {w}")

        with st.spinner("⚡ Evaluating Cardiovascular Logistic Regression Model..."):
            time.sleep(0.4)
            # Feature order: age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal
            feature_array = [form_values[k] for k in features]
            result = predict_disease("heart", feature_array)
            st.session_state["heart_prediction_result"] = result

    # Display Result
    if "heart_prediction_result" in st.session_state:
        st.markdown("<br>", unsafe_allow_html=True)
        render_prediction_result(st.session_state["heart_prediction_result"], "Heart Disease")

    render_disclaimer()
