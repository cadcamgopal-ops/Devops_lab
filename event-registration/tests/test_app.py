import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_register_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Register for the Event" in response.data

def test_successful_registration(client):
    response = client.post("/", data={
        "name": "John Doe",
        "email": "john@example.com",
        "event": "Workshop"
    }, follow_redirects=True)
    assert b"Thank you, John Doe!" in response.data