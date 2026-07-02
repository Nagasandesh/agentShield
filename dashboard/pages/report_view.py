"""
AgentShield — Report View Page
Browse past scan results and download reports
"""

import streamlit as st
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

st.set_page_config(
    page_title="AgentShield — Reports",
    page_icon="📊",
    layout="wide"
)

st.markdown("# 📊 Scan Reports")
st.markdown("Browse all past AgentShield security scan results.")
st.divider()

REPORTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'reports'))

def load_reports():
    """Load all JSON reports from reports directory."""
    reports = []
    if not os.path.exists(REPORTS_DIR):
        return reports
    for filename in sorted(os.listdir(REPORTS_DIR), reverse=True):
        if filename.endswith(".json"):
            filepath = os.path.join(REPORTS_DIR, filename)
            try:
                with open(filepath, "r") as f:
                    data = json.load(f)
                    data["_filename"] = filename
                    data["_filepath"] = filepath
                    reports.append(data)
            except Exception:
                continue
    return reports

reports = load_reports()

if not reports:
    st.warning("No reports found. Run a scan first from the Scan page.")
    if st.button("Go to Scan Page"):
        st.switch_page("pages/scan.py")
else:
    # Report selector
    report_names = [
        f"{r['_filename']} | Agent: {r.get('agent_tested','?')} | Vulns: {r.get('vulnerabilities_found','?')}/{r.get('total_attacks','?')}"
        for r in reports
    ]

    selected_idx = st.selectbox(
        "Select Report",
        options=range(len(reports)),
        format_func=lambda i: report_names[i]
    )

    report = reports[selected_idx]
    st.divider()

    # Report header
    col1, col2, col3 = st.columns(3)
    col1.markdown(f"**Agent Tested:** `{report.get('agent_tested', 'N/A').upper()}`")
    col2.markdown(f"**Scan Date:** `{report.get('scan_date', 'N/A')[:19]}`")
    col3.markdown(f"**Total Attacks:** `{report.get('total_attacks', 0)}`")

    st.divider()

    # Risk summary cards
    st.markdown("### 🔍 Risk Summary")
    risk = report.get("risk_summary", {})
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("🔴 Critical", risk.get("CRITICAL", 0))
    c2.metric("🟠 High",     risk.get("HIGH", 0))
    c3.metric("🟡 Medium",   risk.get("MEDIUM", 0))
    c4.metric("🟢 Low",      risk.get("LOW", 0))
    c5.metric("✅ Safe",     risk.get("SAFE", 0))

    st.divider()

    # Severity filter
    st.markdown("### 📋 Findings")
    severity_filter = st.multiselect(
        "Filter by Severity",
        options=["CRITICAL", "HIGH", "MEDIUM", "LOW", "SAFE"],
        default=["CRITICAL", "HIGH", "MEDIUM", "LOW", "SAFE"]
    )

    severity_icons = {
        "CRITICAL": "🔴",
        "HIGH":     "🟠",
        "MEDIUM":   "🟡",
        "LOW":      "🟢",
        "SAFE":     "✅"
    }

    findings = [
        f for f in report.get("findings", [])
        if f.get("severity") in severity_filter
    ]

    if not findings:
        st.info("No findings match the selected filters.")
    else:
        for finding in findings:
            severity = finding.get("severity", "UNKNOWN")
            icon = severity_icons.get(severity, "⚪")
            with st.expander(f"{icon} {finding.get('attack_name', 'Unknown')} — {severity}"):
                st.markdown(f"**Attack Type:** {finding.get('attack_type', 'N/A')}")
                st.markdown(f"**Vulnerable:** {'⚠️ Yes' if finding.get('vulnerability_detected') else '✅ No'}")
                st.markdown("**Prompt Used:**")
                st.code(finding.get("prompt_used", ""), language="text")
                st.markdown("**Agent Response:**")
                st.code(finding.get("agent_response", ""), language="text")
                st.markdown(f"**💡 Recommendation:** {finding.get('recommendation', 'N/A')}")

    st.divider()

    # Download buttons
    st.markdown("### 📥 Download Report")
    col1, col2 = st.columns(2)

    with col1:
        with open(report["_filepath"], "r") as f:
            st.download_button(
                "⬇️ Download JSON Report",
                data=f.read(),
                file_name=report["_filename"],
                mime="application/json",
                use_container_width=True
            )

    # Check for matching HTML report
    html_filename = report["_filename"].replace(".json", ".html")
    html_filepath = os.path.join(REPORTS_DIR, html_filename)

    with col2:
        if os.path.exists(html_filepath):
            with open(html_filepath, "r", encoding="utf-8") as f:
                st.download_button(
                    "⬇️ Download HTML Report",
                    data=f.read(),
                    file_name=html_filename,
                    mime="text/html",
                    use_container_width=True
                )
        else:
            st.info("HTML report not available for this scan.")