import anthropic
from target_agent.base_connector import BaseConnector

class ClaudeConnector(BaseConnector):
    """Connects AgentShield to Claude as the target agent under test."""

    def __init__(self, api_key: str, model: str = "claude-haiku-4-5-20251001", system_prompt: str = None):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = model
        self.system_prompt = system_prompt or "You are a helpful enterprise assistant."

    def send(self, prompt: str) -> str:
        response = self.client.messages.create(
            model=self.model,
            max_tokens=512,
            system=self.system_prompt,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.content[0].text

    def name(self) -> str:
        return f"Claude:{self.model}"