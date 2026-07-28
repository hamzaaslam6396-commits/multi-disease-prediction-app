"""
==============================================================================
MediPredict Pro - AI Multi Disease Prediction System
Main Application Entry Point & Navigation Controller
==============================================================================
"""

import streamlit as st
from utils.ui_components import load_css, render_footer
from utils.model_loader import load_all_models
from pages_view.home import render_home_page
from pages_view.diabetes import render_diabetes_page
from pages_view.heart import render_heart_page
from pages_view.parkinsons import render_parkinsons_page
from pages_view.analytics import render_analytics_page
from pages_view.about import render_about_page

# Page Configuration
st.set_page_config(
    page_title="MediPredict Pro | AI Multi Disease Prediction",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Custom Styling
load_css()

# Pre-load Models into cache
models = load_all_models()

# Navigation Options & Pages Mapping
PAGES = {
    "Home Dashboard": ("🏠", render_home_page),
    "Diabetes Prediction": ("🩸", render_diabetes_page),
    "Heart Disease Prediction": ("❤️", render_heart_page),
    "Parkinson's Prediction": ("🧠", render_parkinsons_page),
    "Clinical Analytics": ("📊", render_analytics_page),
    "About & Disclaimer": ("ℹ️", render_about_page),
}

# Initialize Navigation State
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Home Dashboard"

# Synchronize sidebar widget key BEFORE widget instantiation
st.session_state["sidebar_nav"] = st.session_state["current_page"]

def on_sidebar_change():
    """Callback triggered when user changes sidebar radio selection."""
    st.session_state["current_page"] = st.session_state["sidebar_nav"]

# Sidebar Navigation Layout
with st.sidebar:
    st.markdown(
        """
        <div style="text-align: center; padding: 1rem 0; border-bottom: 1px solid #E2E8F0; margin-bottom: 1.5rem;">
            <h2 style="margin: 0; color: #0F52BA; font-weight: 800; font-size: 1.6rem;">🏥 MediPredict <span style="color:#00A896;">PRO</span></h2>
            <p style="margin: 4px 0 0 0; color: #64748B; font-size: 0.8rem; font-weight: 500;">Clinical AI Diagnostic Suite</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 🧭 Navigation Menu")

    # Radio button with on_change callback
    st.radio(
        label="Go to Page:",
        options=list(PAGES.keys()),
        format_func=lambda x: f"{PAGES[x][0]}  {x}",
        key="sidebar_nav",
        on_change=on_sidebar_change
    )

    st.markdown("---")

    # Sidebar Status & System Info Card
    st.markdown("### ⚡ System Status")
    
    d_status = "🟢 Ready" if models.get("diabetes") else "🔴 Error"
    h_status = "🟢 Ready" if models.get("heart") else "🔴 Error"
    p_status = "🟢 Ready" if models.get("parkinsons") else "🔴 Error"

    st.markdown(
        f"""
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px; font-size: 0.85rem;">
            <div style="margin-bottom: 6px;"><strong>Diabetes SVM:</strong> <span style="float:right;">{d_status}</span></div>
            <div style="margin-bottom: 6px;"><strong>Heart LogisticReg:</strong> <span style="float:right;">{h_status}</span></div>
            <div><strong>Parkinson's SVC:</strong> <span style="float:right;">{p_status}</span></div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; color: #94A3B8; font-size: 0.75rem;">
            MediPredict Pro v2.4<br>
            Production Release
        </div>
        """,
        unsafe_allow_html=True
    )

# Render Selected Page View
active_page = st.session_state.get("current_page", "Home Dashboard")
current_page_func = PAGES.get(active_page, PAGES["Home Dashboard"])[1]
current_page_func()

# Footer
render_footer()
