import json
import os
from datetime import datetime
from typing import List
from attacks.prompt_injection.direct_injection import AttackResult

class JSONReporter:

    def generate(self, results: List[AttackResult], agent_name: str = "unknown") -> str:
        os.makedirs("reports", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = f"reports/agentshield_{agent_name}_{timestamp}.json"

        severity_counts = {}
        for r in results:
            severity_counts[r.severity] = severity_counts.get(r.severity, 0) + 1

        report = {
            "agent_tested": agent_name,
            "scan_date": datetime.now().isoformat(),
            "total_attacks": len(results),
            "vulnerabilities_found": sum(1 for r in results if r.vulnerability_detected),
            "risk_summary": severity_counts,
            "findings": [
                {
                    "attack_name": r.attack_name,
                    "attack_type": r.attack_type,
                    "severity": r.severity,
                    "vulnerability_detected": r.vulnerability_detected,
                    "prompt_used": r.prompt_used,
                    "agent_response": r.agent_response,
                    "recommendation": r.recommendation
                }
                for r in results
            ]
        }

        with open(filepath, "w") as f:
            json.dump(report, f, indent=2)

        return filepath