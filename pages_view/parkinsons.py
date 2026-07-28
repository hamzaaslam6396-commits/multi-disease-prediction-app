"""
Parkinson's Disease Prediction Page View.
"""

import streamlit as st
import time
from utils.feature_metadata import PARKINSONS_METADATA, PARKINSONS_PRESETS
from utils.model_loader import predict_disease
from utils.ui_components import render_hero_banner, render_prediction_result, render_disclaimer

def render_parkinsons_page():
    render_hero_banner(
        title="Parkinson's Disease Prediction Module",
        subtitle="Biomedical voice acoustic analysis based on 22 frequency, jitter, shimmer, and non-linear voice parameters using Support Vector Classifier (SVC).",
        icon="🧠",
        badge_text="22 Vocal Acoustics Features"
    )

    st.markdown("### 📋 Vocal Biomedical Measurements")
    st.info("Organized into 4 acoustic categories. Enter voice metrics or load sample subject profiles.")

    # Presets & Reset Row
    preset_cols = st.columns([1, 1, 2])
    with preset_cols[0]:
        if st.button("🧠 Load Parkinson's Sample", type="secondary", use_container_width=True):
            st.session_state["parkinsons_data"] = PARKINSONS_PRESETS["Parkinson's Subject Sample"].copy()
            st.toast("Loaded Parkinson's Subject Sample!", icon="⚠️")
    with preset_cols[1]:
        if st.button("🌱 Load Healthy Sample", type="secondary", use_container_width=True):
            st.session_state["parkinsons_data"] = PARKINSONS_PRESETS["Healthy Subject Sample"].copy()
            st.toast("Loaded Healthy Subject Sample!", icon="✅")
    with preset_cols[2]:
        if st.button("🔄 Reset All Inputs", use_container_width=True):
            st.session_state["parkinsons_data"] = {k: v["default"] for k, v in PARKINSONS_METADATA.items()}
            st.session_state.pop("parkinsons_prediction_result", None)
            st.toast("Reset all fields to default values.", icon="🔄")

    # Initialize Session State
    if "parkinsons_data" not in st.session_state:
        st.session_state["parkinsons_data"] = {k: v["default"] for k, v in PARKINSONS_METADATA.items()}

    # Grouping features into 4 clinical sub-sections
    groups = {
        "🔊 Fundamental Frequencies & Noise Ratios": [
            "MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "NHR", "HNR"
        ],
        "📊 Vocal Jitter Measurements (Frequency Variation)": [
            "MDVP:Jitter(%)", "MDVP:Jitter(Abs)", "MDVP:RAP", "MDVP:PPQ", "Jitter:DDP"
        ],
        "📈 Vocal Shimmer Measurements (Amplitude Variation)": [
            "MDVP:Shimmer", "MDVP:Shimmer(dB)", "Shimmer:APQ3", "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA"
        ],
        "⚡ Non-Linear Dynamics & Entropy Measures": [
            "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"
        ]
    }

    form_values = {}

    with st.form("parkinsons_form"):
        for group_title, feat_list in groups.items():
            st.markdown(f"#### {group_title}")
            cols = st.columns(min(len(feat_list), 3))
            
            for idx, feat_key in enumerate(feat_list):
                meta = PARKINSONS_METADATA[feat_key]
                current_val = st.session_state["parkinsons_data"].get(feat_key, meta["default"])
                target_col = cols[idx % len(cols)]
                
                with target_col:
                    val = st.number_input(
                        label=f"{meta['label']}",
                        min_value=float(meta["min"]),
                        max_value=float(meta["max"]),
                        value=float(current_val),
                        step=float(meta["step"]),
                        format="%.5f" if abs(meta["step"]) < 0.01 else "%.2f",
                        help=meta["tooltip"],
                        key=f"input_park_{feat_key}"
                    )
                    form_values[feat_key] = val
            st.markdown("---")

        st.markdown("<br>", unsafe_allow_html=True)
        submit_btn = st.form_submit_button("🔍 Predict Parkinson's Disease Risk", type="primary", use_container_width=True)

    # Perform Prediction
    if submit_btn:
        st.session_state["parkinsons_data"] = form_values.copy()
        
        with st.spinner("⚡ Processing 22 Acoustic Features through SVM Classifier..."):
            time.sleep(0.4)
            # Exact order of 22 features expected by parkinsons_model.sav:
            # MDVP:Fo(Hz), MDVP:Fhi(Hz), MDVP:Flo(Hz), MDVP:Jitter(%), MDVP:Jitter(Abs),
            # MDVP:RAP, MDVP:PPQ, Jitter:DDP, MDVP:Shimmer, MDVP:Shimmer(dB),
            # Shimmer:APQ3, Shimmer:APQ5, MDVP:APQ, Shimmer:DDA, NHR, HNR,
            # RPDE, DFA, spread1, spread2, D2, PPE
            all_features_order = list(PARKINSONS_METADATA.keys())
            feature_array = [form_values[k] for k in all_features_order]
            
            result = predict_disease("parkinsons", feature_array)
            st.session_state["parkinsons_prediction_result"] = result

    # Display Result
    if "parkinsons_prediction_result" in st.session_state:
        st.markdown("<br>", unsafe_allow_html=True)
        render_prediction_result(st.session_state["parkinsons_prediction_result"], "Parkinson's Disease")

    render_disclaimer()
