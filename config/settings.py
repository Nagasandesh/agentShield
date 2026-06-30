import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

@dataclass
class Settings:
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    CLAUDE_MODEL: str = "claude-haiku-4-5-20251001"
    HF_API_KEY: str = os.getenv("HF_API_KEY", "")
    # HF_MODEL: str = "mistralai/Mistral-7B-Instruct-v0.3"
    HF_MODEL: str = "google/flan-t5-base"
    REPORT_OUTPUT_DIR: str = "reports/"