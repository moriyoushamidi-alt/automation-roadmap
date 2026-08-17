from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_service_is_running():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "service is running"


def test_valid_lead():
    response = client.post("/validate-lead", json={
        "name": "Ali",
        "email": "ali@example.com",
        "city": "Tehran"
    })
    assert response.json()["valid"] == True
    assert response.json()["errors"] == []


def test_empty_name():
    response = client.post("/validate-lead", json={
        "name": "",
        "email": "ali@example.com"
    })
    assert response.json()["valid"] == False
    assert "name is empty" in response.json()["errors"]


def test_invalid_email():
    response = client.post("/validate-lead", json={
        "name": "Ali",
        "email": "broken-email"
    })
    assert response.json()["valid"] == False
    assert "invalid email format" in response.json()["errors"]