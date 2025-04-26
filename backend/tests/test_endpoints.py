# tests/test_endpoints.py
from fastapi.testclient import TestClient
import sys
import os

# Add the backend directory to the path so we can import 'app'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app  # Import the FastAPI app instance

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
    assert response.json() == {"status": "ok"}, f"Expected {{'status': 'ok'}}, got {response.json()}"
    print("\nHealth endpoint test passed!")

def test_chat_endpoint_post():
    test_message = "Hello Coding Pet"
    response = client.post(
        "/api/chat",
        json={"message": test_message}
    )
    assert response.status_code == 200, f"Expected 200 OK, got {response.status_code} for POST /api/chat"
    response_data = response.json()
    assert "response" in response_data, f"Expected 'response' key in JSON, got {response_data}"
    # Since we have a mock response, we can assert its exact content
    expected_response = "I'm your coding companion! How can I help you today?"
    assert response_data["response"] == expected_response, f"Expected '{expected_response}', got {response_data['response']}"
    print("\nChat endpoint POST test passed!")

def test_chat_endpoint_get_not_allowed():
    response = client.get("/api/chat")
    assert response.status_code == 405, f"Expected 405 Method Not Allowed, got {response.status_code} for GET /api/chat"
    print("\nChat endpoint GET (Method Not Allowed) test passed!")

# You can add more tests here if needed
