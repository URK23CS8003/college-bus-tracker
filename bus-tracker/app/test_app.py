import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Bus" in response.data

def test_admin_page(client):
    response = client.get("/admin")
    assert response.status_code == 200
    assert b"Admin" in response.data

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert b"healthy" in response.data

def test_api_buses(client):
    response = client.get("/api/buses")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)
    assert len(data) > 0

def test_api_single_bus(client):
    response = client.get("/api/buses/B01")
    assert response.status_code == 200
    data = response.get_json()
    assert "route" in data
    assert "status" in data

def test_api_invalid_bus(client):
    response = client.get("/api/buses/B99")
    assert response.status_code == 404

def test_update_bus_status(client):
    response = client.post("/admin/update", data={"bus_id": "B01", "status": "Delayed"}, follow_redirects=True)
    assert response.status_code == 200

def test_add_announcement(client):
    response = client.post("/admin/announce", data={"message": "Test announcement"}, follow_redirects=True)
    assert response.status_code == 200
