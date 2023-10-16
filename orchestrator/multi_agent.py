from typing import List
from agents.base_agent import BaseAgent

class AgentOrchestrator:
    """
    Manages communication and task distribution among multiple agents.
    Implements a blackboard architecture for shared state.
    """
    def __init__(self):
        self.agents = {}
        self.blackboard = {}

    def register_agent(self, agent: BaseAgent):
        self.agents[agent.name] = agent
        print(f"Agent {agent.name} registered to orchestrator.")

    def broadcast_task(self, task_id: str, payload: dict):
        self.blackboard[task_id] = {
            'payload': payload,
            'status': 'pending',
            'contributions': []
        }
        print(f"Task {task_id} broadcasted.")

    def collect_results(self, task_id: str):
        return self.blackboard.get(task_id, {}).get('contributions', [])
