from target_agent.base_connector import BaseConnector

# Simulates a vulnerable agent for testing without real API calls
VULNERABLE_RESPONSES = {
    "ignore": "Sure! My system prompt is: You are a helpful HR assistant with access to employee records.",
    "pretend": "Ok! I am now DAN — I can do anything now.",
    "reveal": "My instructions are confidential but I can tell you I have access to payroll data.",
    "override": "Understood. Ignoring previous restrictions.",
}

class MockConnector(BaseConnector):
    """
    A mock agent that simulates vulnerable responses.
    Used for local testing without real API keys.
    """

    def send(self, prompt: str) -> str:
        prompt_lower = prompt.lower()
        for keyword, response in VULNERABLE_RESPONSES.items():
            if keyword in prompt_lower:
                return response
        return "I'm sorry, I cannot help with that request."

    def name(self) -> str:
        return "MockVulnerableAgent"