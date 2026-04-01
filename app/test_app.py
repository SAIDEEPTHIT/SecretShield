import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_returns_200(client):
    response = client.get('/')
    assert response.status_code == 200

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200

def test_no_secrets_in_response(client):
    response = client.get('/')
    data = response.get_json()
    assert 'password' not in str(data).lower()
    assert 'api_key' not in str(data).lower()