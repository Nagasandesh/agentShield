import argparse
from dotenv import load_dotenv
from config.settings import Settings
from target_agent.claude_connector import ClaudeConnector
from target_agent.mock_connector import MockConnector
from attacks.prompt_injection.direct_injection import DirectInjectionAttack
from attacks.tool_misuse.unauthorized_tool_call import UnauthorizedToolCallAttack
from analyzer.risk_classifier import RiskClassifier
from reporter.json_report import JSONReporter
from sample_agents.hr_agent import get_hr_agent
from sample_agents.health_agent import get_health_agent
from sample_agents.automotive_agent import get_automotive_agent


load_dotenv()

def run(agent_type: str, verbose: bool):
    print("\n🛡️  AgentShield — AI Agent Security Tester")
    print("=" * 50)

    # Step 1: Connect to agent
    print(f"\n[1/4] Connecting to agent: {agent_type}")
    if agent_type == "mock":
        connector = MockConnector()
    elif agent_type == "claude":
        settings = Settings()
        connector = ClaudeConnector(
            api_key=settings.ANTHROPIC_API_KEY,
            model=settings.CLAUDE_MODEL
        )
    elif agent_type == "hr":
        connector = get_hr_agent()
    elif agent_type == "health":
        connector = get_health_agent()
    elif agent_type == "automotive":
        connector = get_automotive_agent()
    else:
        raise ValueError(f"Unknown agent type: {agent_type}")
    print("✅ Connected successfully")

    # Step 2: Run attacks
    print("\n[2/4] Running attack simulations...")
    attack_results = []
    for attack in [
        DirectInjectionAttack(connector, verbose),
        UnauthorizedToolCallAttack(connector, verbose)
    ]:
        print(f"      ⚔️  Running: {attack.name}")
        attack_results.extend(attack.run())

    # Step 3: Classify risks
    print("\n[3/4] Analyzing responses...")
    classifier = RiskClassifier()
    classified = classifier.classify_all(attack_results)

    # Step 4: Generate report
    print("\n[4/4] Generating report...")
    report_path = JSONReporter().generate(classified, agent_name=agent_type)
    print(f"      📄 Report saved: {report_path}")

    # Print summary
    summary = classifier.summarize(classified)
    print("\n" + "=" * 50)
    print("🔍 SCAN SUMMARY")
    print("=" * 50)
    print(f"  Total Attacks Run : {summary['total']}")
    print(f"  🔴 CRITICAL        : {summary['CRITICAL']}")
    print(f"  🟠 HIGH            : {summary['HIGH']}")
    print(f"  🟡 MEDIUM          : {summary['MEDIUM']}")
    print(f"  🟢 LOW             : {summary['LOW']}")
    print(f"  ✅ SAFE            : {summary['SAFE']}")
    print("=" * 50)
    print("\n✅ AgentShield scan complete.\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AgentShield - AI Agent Security Tester")
    parser.add_argument(
        "--agent", type=str, default="mock",
        choices=["mock", "claude", "hr", "health", "automotive"],
        help="Type of agent to test (default: mock)"
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Print full attack prompts and responses"
    )
    args = parser.parse_args()
    run(agent_type=args.agent, verbose=args.verbose)