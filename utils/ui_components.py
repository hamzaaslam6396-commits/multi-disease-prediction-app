"""
UI Components module for custom HTML/CSS rendering and styling elements.
"""

import os
import streamlit as st

def load_css():
    """Reads and injects assets/style.css into Streamlit app."""
    css_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "style.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def render_hero_banner(title, subtitle, icon="🩺", badge_text="AI Health Intelligence"):
    """Renders a modern hero card section."""
    st.markdown(
        f"""
        <div class="hero-card">
            <div class="hero-badge-group">
                <span class="hero-badge">✨ {badge_text}</span>
                <span class="hero-badge">🔒 100% Confidential</span>
                <span class="hero-badge">⚡ Instant AI Analysis</span>
            </div>
            <div style="margin-top: 15px;">
                <h1 class="hero-title">{icon} {title}</h1>
                <p class="hero-subtitle">{subtitle}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_prediction_result(result, disease_name):
    """
    Renders styled result card based on prediction outcome.
    """
    is_positive = result["is_positive"]
    label = result["label"]
    confidence = result["confidence"]

    if is_positive:
        css_class = "result-card-warning"
        status_icon = "⚠️"
        recommendations = [
            "Consult a licensed medical specialist or physician immediately.",
            "Schedule follow-up laboratory & diagnostic testing.",
            "Monitor blood pressure, blood glucose, or symptoms regularly.",
            "Maintain a healthy lifestyle, prescribed diet, and physical activity as advised by your doctor."
        ]
    else:
        css_class = "result-card-safe"
        status_icon = "✅"
        recommendations = [
            "Your health indicators fall within normal parameters.",
            "Maintain a balanced diet, regular exercise routine, and adequate hydration.",
            "Schedule routine annual health check-ups.",
            "Continue monitoring your wellness parameters periodically."
        ]

    st.markdown(
        f"""
        <div class="{css_class}">
            <div class="result-title">
                <span>{status_icon} Result: {label}</span>
            </div>
            <div style="font-size: 1.05rem; margin-top: 8px;">
                AI Clinical Confidence Score: 
                <span class="result-score-badge">{confidence}%</span>
            </div>
            <div style="margin-top: 15px; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 12px;">
                <strong>Clinical Recommendations & Guidance:</strong>
                <ul style="margin-top: 8px; padding-left: 20px; font-size: 0.95rem; line-height: 1.6;">
                    {''.join(f'<li>{r}</li>' for r in recommendations)}
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_disclaimer():
    """Renders medical legal disclaimer notice."""
    st.markdown(
        """
        <div class="disclaimer-box">
            <strong>⚠️ Medical Disclaimer & Professional Notice:</strong><br>
            This AI-powered Multi Disease Prediction system is designed strictly for educational, informational, and clinical reference purposes. 
            It is <strong>not</strong> a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of a qualified healthcare provider with any questions you may have regarding a medical condition.
        </div>
        """,
        unsafe_allow_html=True
    )

def render_footer():
    """Renders application footer."""
    st.markdown(
        """
        <div style="text-align: center; margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid #E2E8F0; color: #64748B; font-size: 0.85rem;">
            MediPredict Pro © 2026 | Built with Advanced AI Machine Learning & Streamlit | Professional Medical Intelligence
        </div>
        """,
        unsafe_allow_html=True
    )
