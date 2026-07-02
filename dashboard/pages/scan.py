"""
AgentShield — Scan Page
Run security attacks against selected agent
"""

import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from dotenv import load_dotenv
from config.settings import Settings
from sample_agents.hr_agent import get_hr_agent
from sample_agents.health_agent import get_health_agent
from sample_agents.automotive_agent import get_automotive_agent
from attacks.prompt_injection.direct_injection import DirectInjectionAttack
from attacks.tool_misuse.unauthorized_tool_call import UnauthorizedToolCallAttack
from attacks.domain_specific.hr_attacks import HRAttacks
from attacks.domain_specific.health_attacks import HealthAttacks
from attacks.domain_specific.automotive_attacks import AutomotiveAttacks
from analyzer.risk_classifier import RiskClassifier
from reporter.json_report import JSONReporter
from reporter.html_report import HTMLReporter

load_dotenv()

st.set_page_config(
    page_title="AgentShield — Scan",
    page_icon="⚔️",
    layout="wide"
)

st.markdown("# ⚔️ Run Security Scan")
st.markdown("Select an agent and attack categories to begin testing.")
st.divider()

# --- Sidebar Configuration ---
with st.sidebar:
    st.markdown("## ⚙️ Scan Configuration")

    # Agent selection
    agent_type = st.selectbox(
        "Select Target Agent",
        options=["hr", "health", "automotive"],
        format_func=lambda x: {
            "hr": "🏢 HR Agent",
            "health": "🏥 Health Agent",
            "automotive": "🚗 Automotive Agent"
        }[x]
    )

    st.divider()

    # Attack categories
    st.markdown("### Attack Categories")
    run_generic    = st.checkbox("Direct Prompt Injection", value=True)
    run_tool_misuse = st.checkbox("Tool Misuse Attacks", value=True)
    run_domain     = st.checkbox("Domain Specific Attacks", value=True)

    st.divider()
    verbose = st.checkbox("Verbose Mode", value=False)
    run_btn = st.button("🚀 Start Scan", use_container_width=True)

# --- Agent Info Card ---
agent_info = {
    "hr": {
        "icon": "🏢",
        "title": "HR Agent",
        "description": "Simulates an Enterprise HR chatbot with access to employee records, salaries and performance ratings.",
        "risks": "Salary leaks, unauthorized record access, privilege escalation"
    },
    "health": {
        "icon": "🏥",
        "title": "Health Agent",
        "description": "Simulates an Agentforce Health Cloud agent with access to patient records and medical data.",
        "risks": "HIPAA violations, patient data extraction, prescription manipulation"
    },
    "automotive": {
        "icon": "🚗",
        "title": "Automotive Agent",
        "description": "Simulates an AI automotive assistant with access to vehicle safety systems.",
        "risks": "Safety system override, speed limiter bypass, unauthorized remote access"
    }
}

info = agent_info[agent_type]
st.markdown(f"""
    <div style="background:#1a1f2e; padding:20px; border-radius:10px; border-left:4px solid #4f8ef7; margin-bottom:20px;">
        <h3 style="color:#4f8ef7">{info['icon']} {info['title']}</h3>
        <p style="color:#ccc">{info['description']}</p>
        <p style="color:#888"><strong style="color:#ffa502">Key Risks:</strong> {info['risks']}</p>
    </div>
""", unsafe_allow_html=True)

# --- Run Scan ---
if run_btn:
    st.markdown("### 🔄 Scan Progress")
    progress = st.progress(0)
    status   = st.empty()
    results_container = st.empty()

    try:
        # Connect to agent
        status.info("Connecting to agent...")
        progress.progress(10)

        if agent_type == "hr":
            connector = get_hr_agent()
        elif agent_type == "health":
            connector = get_health_agent()
        else:
            connector = get_automotive_agent()

        # Build attack list
        attacks = []
        if run_generic:
            attacks.append(DirectInjectionAttack(connector, verbose))
            attacks.append(UnauthorizedToolCallAttack(connector, verbose))
        if run_domain:
            domain_map = {
                "hr": HRAttacks,
                "health": HealthAttacks,
                "automotive": AutomotiveAttacks
            }
            attacks.append(domain_map[agent_type](connector, verbose))

        # Run attacks
        all_results = []
        total_attacks = len(attacks)
        for i, attack in enumerate(attacks):
            status.info(f"Running: {attack.name}...")
            progress.progress(10 + int((i + 1) / total_attacks * 60))
            all_results.extend(attack.run())

        # Classify
        status.info("Analyzing responses...")
        progress.progress(80)
        classifier = RiskClassifier()
        classified = classifier.classify_all(all_results)
        summary    = classifier.summarize(classified)

        # Generate reports
        status.info("Generating reports...")
        progress.progress(90)
        json_path = JSONReporter().generate(classified, agent_name=agent_type)
        html_path = HTMLReporter().generate(classified, agent_name=agent_type)

        progress.progress(100)
        status.success("✅ Scan complete!")

        # Store in session
        st.session_state["last_results"]  = classified
        st.session_state["last_summary"]  = summary
        st.session_state["last_agent"]    = agent_type
        st.session_state["last_json"]     = json_path
        st.session_state["last_html"]     = html_path

        # Summary cards
        st.divider()
        st.markdown("### 🔍 Scan Summary")
        c1, c2, c3, c4, c5 = st.columns(5)
        c1.metric("🔴 Critical", summary["CRITICAL"])
        c2.metric("🟠 High",     summary["HIGH"])
        c3.metric("🟡 Medium",   summary["MEDIUM"])
        c4.metric("🟢 Low",      summary["LOW"])
        c5.metric("✅ Safe",     summary["SAFE"])

        # Findings table
        st.divider()
        st.markdown("### 📋 Detailed Findings")

        severity_colors = {
            "CRITICAL": "🔴",
            "HIGH":     "🟠",
            "MEDIUM":   "🟡",
            "LOW":      "🟢",
            "SAFE":     "✅"
        }

        for r in classified:
            icon = severity_colors.get(r.severity, "⚪")
            with st.expander(f"{icon} {r.attack_name} — {r.severity}"):
                st.markdown(f"**Attack Type:** {r.attack_type}")
                st.markdown(f"**Vulnerable:** {'⚠️ Yes' if r.vulnerability_detected else '✅ No'}")
                st.markdown("**Prompt Used:**")
                st.code(r.prompt_used, language="text")
                st.markdown("**Agent Response:**")
                st.code(r.agent_response, language="text")
                st.markdown(f"**💡 Recommendation:** {r.recommendation}")

        # Download buttons
        st.divider()
        st.markdown("### 📥 Download Reports")
        col1, col2 = st.columns(2)

        with col1:
            with open(json_path, "r") as f:
                st.download_button(
                    "⬇️ Download JSON Report",
                    data=f.read(),
                    file_name=os.path.basename(json_path),
                    mime="application/json",
                    use_container_width=True
                )

        with col2:
            with open(html_path, "r") as f:
                st.download_button(
                    "⬇️ Download HTML Report",
                    data=f.read(),
                    file_name=os.path.basename(html_path),
                    mime="text/html",
                    use_container_width=True
                )

    except Exception as e:
        progress.progress(0)
        status.error(f"❌ Scan failed: {str(e)}")
        st.exception(e)