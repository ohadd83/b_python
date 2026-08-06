from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_root():

    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Hello from Jenkins CI/CD FastAPI application test num 1"



def test_health():

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"



def test_version():

    response = client.get("/version")

    assert response.status_code == 200
    assert response.json()["version"] == "1.0.0"
