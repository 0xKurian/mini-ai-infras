from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "host" in data

def test_predict():
    response = client.get("/predict?text=hello")
    assert response.status_code == 200
    assert response.json() == {
        "input": "hello",
        "prediction": "AI_processed_HELLO"
    }