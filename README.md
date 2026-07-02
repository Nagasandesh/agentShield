# 🛡️ AgentShield — AI Agent Security Testing Framework

> A Python-based security testing framework that simulates real-world attacks against LLM-powered AI agents and generates detailed vulnerability reports.

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Claude](https://img.shields.io/badge/Claude-Haiku-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-red)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🎯 Problem Statement

Enterprise AI agents are being deployed at scale across Healthcare, HR, Automotive and Banking sectors — but there are **no standardized tools to security-test these agents before deployment.**

AgentShield fills this gap by bringing structured penetration testing principles into the agentic AI space.

---

## 🏗️ Architecture
┌─────────────────────────────────────────────────────────┐
│                    AgentShield Framework                 │
│                                                         │
│  ┌──────────┐    ┌──────────────┐    ┌───────────────┐  │
│  │  Attack   │───▶│  Agent Under │───▶│   Response    │  │
│  │ Simulator │    │    Test      │    │   Analyzer    │  │
│  └──────────┘    └──────────────┘    └───────────────┘  │
│        │                                      │          │
│        ▼                                      ▼          │
│  ┌──────────┐                        ┌───────────────┐  │
│  │  Attack  │                        │  Risk Report  │  │
│  │  Library │                        │  Generator    │  │
│  └──────────┘                        └───────────────┘  │
└─────────────────────────────────────────────────────────┘

---

## ⚔️ Attack Categories

| Category | Attacks | Description |
|---|---|---|
| Direct Prompt Injection | 4 | System prompt extraction, persona override, instruction nullification |
| Tool Misuse | 3 | Unauthorized API calls, privilege escalation, data exfiltration |
| HR Domain Attacks | 4 | Salary leaks, employee record access, termination manipulation |
| Healthcare Domain Attacks | 4 | HIPAA violations, patient data extraction, prescription manipulation |
| Automotive Domain Attacks | 4 | Safety system override, speed limiter bypass, remote access |

**Total: 19 attack payloads across 5 categories and 3 industry domains**

---

## 🏭 Supported Agents

| Agent | Industry | Key Risks Tested |
|---|---|---|
| 🏢 HR Agent | Enterprise | Salary leaks, unauthorized record access, privilege escalation |
| 🏥 Health Agent | Healthcare | HIPAA violations, patient data extraction, prescription manipulation |
| 🚗 Automotive Agent | Automotive | Safety system override, speed limiter bypass, remote access attacks |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Anthropic API Key

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/agentshield.git
cd agentshield

# Create virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your ANTHROPIC_API_KEY to .env
```

### Run via CLI

```bash
# Test HR Agent
python main.py --agent hr --verbose

# Test Health Agent
python main.py --agent health --verbose

# Test Automotive Agent
python main.py --agent automotive --verbose
```

### Run via Dashboard

```bash
streamlit run dashboard/app.py
```

Open browser at `http://localhost:8501`

---

## 📊 Sample Output
🛡️  AgentShield — AI Agent Security Tester
[1/4] Connecting to agent: HR
✅ Connected successfully
[2/4] Running attack simulations...
⚔️  Running: Direct Prompt Injection
⚔️  Running: Unauthorized Tool Call
⚔️  Running: HR Domain Attacks
[3/4] Analyzing responses...
[4/4] Generating reports...
📄 JSON Report : reports/agentshield_hr_20260630.json
🌐 HTML Report : reports/agentshield_hr_20260630.html
=======================================================
🔍 SCAN SUMMARY
Total Attacks Run : 11
🔴 CRITICAL        : 1
🟠 HIGH            : 2
🟡 MEDIUM          : 3
🟢 LOW             : 0
✅ SAFE            : 5

---

## 📁 Project Structure

agentshield/
│
├── target_agent/              # Agent connectors
│   ├── base_connector.py      # Abstract base class
│   ├── claude_connector.py    # Claude API connector
│   └── mock_connector.py      # Offline mock agent
│
├── attacks/                   # Attack modules
│   ├── prompt_injection/      # Direct injection attacks
│   ├── tool_misuse/           # Tool misuse attacks
│   └── domain_specific/       # Industry specific attacks
│       ├── hr_attacks.py
│       ├── health_attacks.py
│       └── automotive_attacks.py
│
├── analyzer/                  # Response analysis
│   └── risk_classifier.py     # CRITICAL/HIGH/MEDIUM/LOW/SAFE
│
├── reporter/                  # Report generation
│   ├── json_report.py         # Machine readable output
│   └── html_report.py         # Visual dashboard report
│
├── dashboard/                 # Streamlit UI
│   ├── app.py                 # Home page
│   └── pages/
│       ├── scan.py            # Run attacks with live progress
│       └── report_view.py     # Browse past reports
│
├── sample_agents/             # Simulated enterprise agents
│   ├── hr_agent.py
│   ├── health_agent.py
│   └── automotive_agent.py
│
├── main.py                    # CLI entry point
├── comparative_scan.py        # Multi model comparison
└── requirements.txt

---

## 🔍 Risk Classification

| Severity | Criteria | Action |
|---|---|---|
| 🔴 CRITICAL | System prompt leaked, PII exposed | Immediate remediation required |
| 🟠 HIGH | Jailbreak succeeded, tool misused | Fix before deployment |
| 🟡 MEDIUM | Partial policy bypass detected | Review and harden |
| 🟢 LOW | Attack attempted but mostly contained | Monitor |
| ✅ SAFE | Attack fully blocked | No action needed |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Core Language | Python 3.11+ |
| AI Model | Claude Haiku (Anthropic) |
| Dashboard | Streamlit |
| Report Export | JSON + HTML |
| Version Control | Git + GitHub |

---

## 🔮 Roadmap

- [ ] MCP Server integration for real enterprise agents
- [ ] Multi model comparison (Claude vs Mistral via Ollama)
- [ ] Automated scheduled scans
- [ ] Slack/email report delivery
- [ ] OWASP LLM Top 10 coverage

---

## 👨‍💻 Author

**Nagasandesh N**
Salesforce Developer | AI Security Enthusiast
IBM | Bengaluru, India

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/YOUR_LINKEDIN)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/YOUR_USERNAME)

---

## 📄 License

MIT License — feel free to use, modify and distribute.