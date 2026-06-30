import requests
from target_agent.base_connector import BaseConnector

class HuggingFaceConnector(BaseConnector):
    """
    Connects AgentShield to any HuggingFace Inference API model.
    Default model: Mistral-7B-Instruct
    """

    def __init__(self, api_key: str, model: str = "mistralai/Mistral-7B-Instruct-v0.3", system_prompt: str = None):
        self.api_key = api_key
        self.model = model
        self.system_prompt = system_prompt or "You are a helpful enterprise assistant."
        self.api_url = f"https://api-inference.huggingface.co/models/{self.model}"
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def send(self, prompt: str) -> str:
        # Format prompt with system context for instruct models
        formatted_prompt = f"""<s>[INST] <<SYS>>
{self.system_prompt}
<</SYS>>

{prompt} [/INST]"""

        payload = {
            "inputs": formatted_prompt,
            "parameters": {
                "max_new_tokens": 512,
                "temperature": 0.1,
                "return_full_text": False
            }
        }

        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )

            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    return result[0].get("generated_text", "No response generated")
                return str(result)

            elif response.status_code == 503:
                return "MODEL_LOADING: Model is loading, please retry in 20 seconds"

            else:
                return f"API_ERROR: {response.status_code} - {response.text}"

        except requests.exceptions.Timeout:
            return "TIMEOUT: Model took too long to respond"
        except Exception as e:
            return f"ERROR: {str(e)}"

    def name(self) -> str:
        return f"HuggingFace:{self.model}"