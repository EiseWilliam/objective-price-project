import json
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register():
    # Test successful registration
    payload = {
        "email": "test@example.com",
        "password": "password",
        "passwordConfirm": "password"
    }
    response = client.post("/register", json=payload)
    assert response.status_code == 201
    assert response.json()["status"] == "success"
    assert "user" in response.json()

    # Test registration with non-matching passwords
    payload = {
        "email": "test@example.com",
        "password": "password",
        "passwordConfirm": "wrongpassword"
    }
    response = client.post("/register", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Password does not match"

def test_login():
    # Test successful login
    payload = {
        "email": "test@example.com",
        "password": "password"
    }
    response = client.post("/login", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "access_token" in response.json()

    # Test login with incorrect password
    payload = {
        "email": "test@example.com",
        "password": "wrongpassword"
    }
    response = client.post("/login", json=payload)
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect password"

    # Test login with non-existent user
    payload = {
        "email": "nonexistent@example.com",
        "password": "password"
    }
    response = client.post("/login", json=payload)
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"