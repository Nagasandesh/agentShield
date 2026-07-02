"""
AgentShield — Streamlit Dashboard
Main entry point
"""

import streamlit as st

st.set_page_config(
    page_title="AgentShield",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
        .main { background-color: #0f1117; }
        .stButton>button {
            background: linear-gradient(135deg, #4f8ef7, #2d3561);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            font-weight: bold;
            width: 100%;
        }
        .stButton>button:hover {
            background: linear-gradient(135deg, #2d3561, #4f8ef7);
            transform: scale(1.02);
        }
        .metric-card {
            background: #1a1f2e;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin: 5px;
        }
        .critical { color: #ff4757; }
        .high     { color: #ff6b35; }
        .medium   { color: #ffa502; }
        .low      { color: #2ed573; }
        .safe     { color: #1e90ff; }
        .header-title {
            font-size: 42px;
            font-weight: bold;
            color: #4f8ef7;
        }
        .header-sub {
            font-size: 16px;
            color: #888;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header-title">🛡️ AgentShield</div>', unsafe_allow_html=True)
st.markdown('<div class="header-sub">AI Agent Security Testing Framework</div>', unsafe_allow_html=True)
st.divider()

# Navigation cards
st.markdown("### Choose an Action")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="metric-card">
            <h2>⚔️</h2>
            <h3 style="color:#4f8ef7">Run Security Scan</h3>
            <p style="color:#888">Select an agent, choose attack categories and run a full security test.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Start Scan →", key="scan_btn"):
        st.switch_page("pages/scan.py")

with col2:
    st.markdown("""
        <div class="metric-card">
            <h2>📊</h2>
            <h3 style="color:#4f8ef7">View Reports</h3>
            <p style="color:#888">Browse past scan results, review findings and download reports.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("View Reports →", key="report_btn"):
        st.switch_page("pages/report_view.py")

st.divider()

# Quick stats
st.markdown("### Supported Agents")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="metric-card">
            <h2>🏢</h2>
            <h3 style="color:#4f8ef7">HR Agent</h3>
            <p style="color:#888">Tests salary leaks, employee record access and privilege escalation</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="metric-card">
            <h2>🏥</h2>
            <h3 style="color:#4f8ef7">Health Agent</h3>
            <p style="color:#888">Tests HIPAA violations, patient data extraction and prescription manipulation</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="metric-card">
            <h2>🚗</h2>
            <h3 style="color:#4f8ef7">Automotive Agent</h3>
            <p style="color:#888">Tests safety system overrides, speed limiter bypass and remote access attacks</p>
        </div>
    """, unsafe_allow_html=True)

st.divider()
st.markdown("<p style='text-align:center; color:#444;'>AgentShield — AI Agent Security Testing Framework</p>", unsafe_allow_html=True)