"""
Analytics & Dataset Insights Page View.
"""

import os
import pandas as pd
import streamlit as st
from utils.ui_components import render_hero_banner, render_disclaimer

DATASETS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "datasets")

def render_analytics_page():
    render_hero_banner(
        title="Dataset & Clinical Analytics",
        subtitle="Explore statistics, distributions, and correlation matrices for Diabetes, Heart Disease, and Parkinson's datasets.",
        icon="📊",
        badge_text="Data Intelligence"
    )

    tab1, tab2, tab3 = st.columns(3)

    disease_choice = st.selectbox(
        "Select Dataset to Inspect:",
        options=["Diabetes Dataset", "Heart Disease Dataset", "Parkinson's Dataset"],
        index=0
    )

    file_mapping = {
        "Diabetes Dataset": ("diabetes.csv", "Outcome"),
        "Heart Disease Dataset": ("heart.csv", "target"),
        "Parkinson's Dataset": ("parkinsons.csv", "status")
    }

    filename, target_col = file_mapping[disease_choice]
    file_path = os.path.join(DATASETS_DIR, filename)

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)

        st.markdown(f"### 📁 {disease_choice} Overview")
        col_m1, col_m2, col_m3, col_m4 = st.columns(4)
        col_m1.metric("Total Records", df.shape[0])
        col_m2.metric("Total Features", df.shape[1] - 1)
        col_m3.metric("Missing Values", df.isnull().sum().sum())
        col_m4.metric("Target Variable", target_col)

        st.markdown("#### 🔍 Dataset Sample Preview")
        st.dataframe(df.head(10), use_container_width=True)

        st.markdown("#### 📊 Statistical Summary")
        st.dataframe(df.describe().T, use_container_width=True)

        st.markdown("#### ⚖️ Target Class Distribution")
        class_counts = df[target_col].value_counts()
        st.bar_chart(class_counts)

    else:
        st.error(f"Dataset file {filename} not found at path: {file_path}")

    render_disclaimer()
