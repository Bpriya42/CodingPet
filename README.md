# CodingPet

Hey! This is a project I’ve been meaning to start for a while. I love gamifying my tasks to give me that little dopamine boost to actually get things done, lol. So I thought — what if I combined that with a cute pet, some fun colors, a funner personality, *and* something that actually helps me keep my skills sharp? Helllllsss yaaa!

It's giving Jarvis for CS students ( but not as cool xD ... yet )

( Ask me about my Iron Man obsession later )

## Project Description

**CodingPet** is an AI-driven “digital coding companion” designed to keep you company and help you learn to code at your own pace. It provides context-aware, conversational support—reminding you of past interactions, offering hints and explanations, and even cracking a programming joke when you need a break. It is meant to provide companionship, support during long coding sessions, while also encouraging a growth mindset. 

Built with a fully free local stack, CodingPet uses:

- **FastAPI** for a lightning-fast, async HTTP API  
- **LangChain** to orchestrate prompts and chains  
- **Mistral 7B** (via Ollama) as the core language model  
- **ChromaDB** for long-term vector-based memory storage  

The architecture is model-agnostic—later you can swap in any paid LLM (GPT-4, Claude 3, etc.) by changing a single configuration. This makes CodingPet both **easy to extend** and **future-proof**, while giving students a zero-cost way to get started today.

## Project Status
**Last Updated:** June 6, 2024

### Current Progress
- ✅ Initialized Python project using Poetry for dependency management
- ✅ Created a structured backend application with FastAPI
- ✅ Implemented core API endpoints:
  - `GET /health` - Health check endpoint
  - `POST /api/chat` - Chat endpoint (currently returns mock responses)
- ✅ Set up automated testing with pytest
- ✅ Configured development environment with hot-reloading

### Next Steps
- Implement actual language model integration
- Expand API functionality
- Add frontend interface
- Add authentication and user management

## Key Learnings
- Poetry dependency management best practices on Windows
- FastAPI routing and endpoint configuration
- Test-driven development using FastAPI's TestClient
- Environment debugging and dependency resolution
- Managing Python project structure and imports

## Setup Instructions

### Prerequisites
- Python 3.10 or higher
- Poetry

### Installation
1. Clone the repository
```bash
git clone <repository-url>
cd CodingPet
```

2. Install dependencies using Poetry
```bash
poetry install
```

## Running the Application
From the project root directory:
```bash
cd backend
poetry run python -m uvicorn app.main:app --reload
```

The API will be available at http://127.0.0.1:8000

## Testing
Run the tests from the project root:
```bash
poetry run pytest -s
```

## Project Structure
```
CodingPet/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── endpoints.py
│   │   ├── services/
│   │   │   └── chat_service.py
│   │   ├── main.py
│   │   └── modelmanager.py
│   └── tests/
│       └── test_endpoints.py
└── pyproject.toml
```