# backend/app/main.py

from fastapi import FastAPI
from app.api.endpoints import router as chat_router

app = FastAPI(title="CodingPet API")

app.include_router(chat_router, prefix="/api")

@app.get("/health")
async def health_check():
    return {"status": "ok"}
