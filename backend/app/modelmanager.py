# backend/app/modelmanager.py

class ModelManager:
    def __init__(self, model_name: str = None):
        self.model_name = model_name or "mock-model"

    def run(self, prompt: str) -> str:
        # Simple mock response
        return "I'm your coding companion! How can I help you today?"
