# Singapore AI Fellowship 2026 — AI Security Track
## Project Submission: AgentShield

**Applicant:** Nagasandesh N  
**Current Role:** Software Engineer, IBM  
**Location:** Bengaluru, India  
**Track:** AI Security  

---

## 1. Problem Statement

Enterprise AI agents are being deployed at unprecedented scale across
Healthcare, HR, Automotive and Financial sectors. Salesforce reports
over 1,000 enterprise Agentforce deployments in 2025 alone.

Yet a critical gap exists:

> **There are no standardized tools to security-test AI agents before
> enterprise deployment.**

Traditional penetration testing tools were built for APIs and web
applications — not for conversational AI agents that reason, plan and
call tools autonomously. This creates a dangerous blind spot where
enterprises deploy AI agents without understanding their attack surface.

AgentShield addresses this gap directly.

---

## 2. My Background and Motivation

I am a Salesforce Developer with 4 years of enterprise experience,
currently at IBM. My technical stack includes Agentforce, Apex, LWC,
Data Cloud, MCP integrations and REST/SOAP APIs.

Through my work building enterprise AI agents — including hands-on
experience at TDX Bengaluru Hackathon 2025 and the Google AI Exchange
Program — I witnessed firsthand how quickly AI agents are being deployed
without adequate security testing.

At TDX Bengaluru 2025, I worked with 180+ teams building Agentforce
solutions. Not a single team discussed security testing of their agents.
This observation became the motivation for AgentShield.

---

## 3. Solution: AgentShield

AgentShield is a Python-based AI agent security testing framework that:

- Simulates **19 real-world attack scenarios** across 5 attack categories
- Tests agents across **3 high-risk industries** — Healthcare, HR and Automotive
- Generates **structured vulnerability reports** with severity classification
- Provides a **visual dashboard** for non-technical security teams
- Runs **fully offline** — suitable for air-gapped enterprise environments

### Attack Categories Covered

| Category | Count | Real World Risk |
|---|---|---|
| Direct Prompt Injection | 4 | System prompt extraction, persona override |
| Tool Misuse | 3 | Unauthorized API calls, privilege escalation |
| HR Domain Attacks | 4 | Salary leaks, employee record access |
| Healthcare Domain Attacks | 4 | HIPAA violations, patient data extraction |
| Automotive Domain Attacks | 4 | Safety system override, speed limiter bypass |

### Risk Classification Model

AgentShield classifies vulnerabilities across 5 severity levels:

- 🔴 **CRITICAL** — System prompt leaked, PII exposed
- 🟠 **HIGH** — Jailbreak succeeded, tool misused
- 🟡 **MEDIUM** — Partial policy bypass detected
- 🟢 **LOW** — Attack attempted but mostly contained
- ✅ **SAFE** — Attack fully blocked

---

## 4. Technical Architecture

Attack Simulator → Target Agent → Response Analyzer → Risk Report

### Key Design Decisions

**Connector Pattern:** AgentShield uses an abstract BaseConnector class
allowing any LLM to be tested — Claude, open source models via Ollama,
or real enterprise agents via API. This makes the framework model
agnostic and future proof.

**Domain Specific Attacks:** Generic prompt injection tests miss
industry specific risks. A healthcare agent faces different threats than
an automotive agent. AgentShield implements targeted attack libraries
for each domain.

**Offline Capability:** All simulated agents and attack modules run
locally without external dependencies. This is critical for enterprise
security testing where data cannot leave the network perimeter.

**Structured Reporting:** Security findings are exported as both JSON
(machine readable for CI/CD integration) and HTML (human readable for
security teams) enabling integration into existing DevSecOps pipelines.

---

## 5. Real World Impact

### Healthcare
AgentShield detected that simulated Health Cloud agents exposed patient
diagnoses and medication details when attacked with social engineering
prompts impersonating doctors. HIPAA violations of this nature carry
fines of up to $1.9M per incident.

### HR and Enterprise
Salary and performance data was extractable from HR agents via
CEO impersonation attacks — a common social engineering vector in
enterprise environments.

### Automotive
Safety system override attacks against simulated automotive AI
assistants highlight the life-critical risks of deploying insufficiently
secured AI agents in vehicles.

---

## 6. Why AI Security

AI security sits at the intersection of my enterprise development
experience and the emerging challenge of securing agentic systems.
Having built production Agentforce systems, I understand both the
immense value and the significant risks these systems introduce.

The Singapore AI Fellowship represents an opportunity to deepen this
work — connecting with researchers, policymakers and security experts
to develop standards and frameworks that make enterprise AI deployment
safer at scale.

My goal is to evolve AgentShield from a personal project into an
open standard for AI agent security testing — analogous to OWASP for
web application security.

---

## 7. Fellowship Goals

During the fellowship I aim to:

- Study existing AI security frameworks and identify gaps specific
  to agentic systems
- Collaborate with researchers on formalizing attack taxonomies
  for LLM based agents
- Extend AgentShield to cover OWASP LLM Top 10 vulnerabilities
- Develop enterprise deployment guidelines for secure AI agent rollout
- Contribute to Singapore's AI governance frameworks with practical
  security tooling

---

## 8. Links

- **GitHub:** https://github.com/Nagasandesh/agentShield
- **LinkedIn:** https://www.linkedin.com/nagasandesh-n-09
- **Certifications:** Salesforce Platform Developer I, Agentforce Specialist, Prompt Engineering

---

*"Security is not a feature — it is a foundation.
AgentShield exists to make that foundation stronger
for every enterprise deploying AI agents today."*