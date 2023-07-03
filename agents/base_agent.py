import abc
from typing import List, Dict, Any

class BaseAgent(abc.ABC):
    """
    Abstract base class for autonomous LLM agents.
    Defines the core interface for perception, reasoning, and action.
    """
    def __init__(self, name: str, model_config: Dict[str, Any]):
        self.name = name
        self.config = model_config
        self.memory_buffer = []

    @abc.abstractmethod
    def perceive(self, observation: Any):
        pass

    @abc.abstractmethod
    def reason(self) -> str:
        pass

    @abc.abstractmethod
    def act(self, thought: str) -> Any:
        pass

    def update_memory(self, entry: Dict[str, str]):
        self.memory_buffer.append(entry)
        if len(self.memory_buffer) > self.config.get('max_memory', 50):
            self.memory_buffer.pop(0)
