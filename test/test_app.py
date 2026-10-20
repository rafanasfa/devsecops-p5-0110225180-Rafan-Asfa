import pytest
from src.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['message'] == "DevSecOps Python Practice API is running"

def test_get_all_users(client):
    response = client.get('/api/users')
    assert response.status_code == 200
    assert len(response.json['data']) > 0

def test_get_user_not_found(client):
    response = client.get('/api/users/999')
    assert response.status_code == 404