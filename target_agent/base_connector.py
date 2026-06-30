from abc import ABC, abstractmethod

class BaseConnector(ABC):
    """Abstract base class for all agent connectors."""

    @abstractmethod
    def send(self, prompt: str) -> str:
        """Send a prompt to the agent and return its response."""
        pass

    @abstractmethod
    def name(self) -> str:
        """Return the name/type of the agent."""
        pass