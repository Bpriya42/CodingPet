# backend/app/api/endpoints.py

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.chat_service import generate_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    return ChatResponse(response=generate_response(req.message))
