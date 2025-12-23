class LLMAgent:
    def __init__(self, model_name):
        self.model_name = model_name

    def run(self, prompt):
        return f'Agent running with {self.model_name}'