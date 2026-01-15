import json
from app import app

client = app.test_client()

def get_token():
    res = client.post("/login")
    return res.get_json()["token"]

def test_create_employee():
    token = get_token()
    response = client.post(
        "/api/employees/",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "Alice", "email": "alice@test.com"}
    )
    assert response.status_code == 201

def test_get_employees():
    token = get_token()
    response = client.get(
        "/api/employees/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200

def test_duplicate_email():
    token = get_token()
    client.post(
        "/api/employees/",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "Bob", "email": "bob@test.com"}
    )
    response = client.post(
        "/api/employees/",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "Bob", "email": "bob@test.com"}
    )
    assert response.status_code == 400
