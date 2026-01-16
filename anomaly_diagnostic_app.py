import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 1. Page Styling
st.set_page_config(page_title="Eng. Sulaiman | Anomaly AI", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    [data-testid="stMetricValue"] {
        color: #00f2ff !important;
        text-shadow: 0 0 10px #00f2ff;
    }
    .status-box {
        padding: 20px; border-radius: 10px; text-align: center;
        margin-bottom: 20px; border: 1px solid #30363d;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Header
st.markdown("""
    <div style="background: linear-gradient(90deg, #1f4037 0%, #99f2c8 100%); padding:20px; border-radius:15px; text-align:center;">
        <h1 style="color:black; margin:0;">🧠 AI ANOMALY DETECTOR & ROOT CAUSE ANALYZER</h1>
        <h3 style="color:#004d40; margin:5px 0;">Designed by: Eng. Sulaiman Kudaimi</h3>
    </div>
    """, unsafe_allow_html=True)

# 3. Sidebar Configuration
st.sidebar.title("🛠️ Asset Control")
st.sidebar.markdown("**Monitoring Station:** Pump-01")
threshold = st.sidebar.slider("Vibration Alert Threshold", 0.0, 1.0, 0.75)
st.sidebar.divider()

# 4. Simulation of Live Data (بناءً على التحليل الذي قمت به)
st.divider()
col1, col2, col3, col4 = st.columns(4)

# قيم افتراضية بناءً على نتائجك المذهلة
health_score = 82 
vibration_level = 0.45
pressure_stability = "STABLE"

with col1:
    st.metric("Equipment Health", f"{health_score}%", delta="-3% Last 24h")
with col2:
    st.metric("Vibration (Sensor 10)", f"{vibration_level} g", delta="Increasing")
with col3:
    st.metric("Flow Stability", pressure_stability)
with col4:
    st.metric("Next Maintenance", "14 Days", delta="URGENT", delta_color="inverse")

# 5. Diagnostic Engine (المنطق الذي طلبته)
st.markdown("### 🔍 Root Cause Diagnostic Hub")
diag_col1, diag_col2 = st.columns([2, 1])

with diag_col1:
    # رسم بياني تفاعلي متقدم
    t = np.linspace(0, 100, 100)
    sig = np.sin(t/5) + np.random.normal(0, 0.1, 100)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=sig, name="Vibration Signature", line=dict(color='#00f2ff')))
    fig.add_hline(y=threshold, line_dash="dash", line_color="red", annotation_text="Danger Limit")
    fig.update_layout(template="plotly_dark", height=400, margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(fig, use_container_width=True)

with diag_col2:
    if vibration_level > 0.4:
        st.warning("⚠️ **ANOMALY DETECTED**")
        st.write("**Probable Cause:** Early Bearing Degradation")
        st.write("**Confidence Level:** 87%")
        st.markdown("""
        **Recommended Actions:**
        1. Check Lubrication Levels.
        2. Inspect Bearing Housing for Heat.
        3. Schedule Vibration Analysis Team.
        """)
    else:
        st.success("✅ **SYSTEM NORMAL**")
        st.write("All parameters within operational envelope.")

# 6. Footer
st.markdown(f"""
    <div style="text-align:center; padding:20px; color:#8b949e; border-top:1px solid #30363d;">
        Predictive Maintenance Solutions | <b>Eng. Sulaiman Kudaimi</b> © 2024
    </div>
    """, unsafe_allow_html=True)