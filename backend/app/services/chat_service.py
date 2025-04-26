# backend/app/services/chat_service.py

from app.modelmanager import ModelManager

_manager = ModelManager()

def generate_response(user_input: str) -> str:
    system = "You are a friendly coding companion. Keep answers clear and concise."
    prompt = f"{system}\n\nStudent: {user_input}\nPet:"
    return _manager.run(prompt) 