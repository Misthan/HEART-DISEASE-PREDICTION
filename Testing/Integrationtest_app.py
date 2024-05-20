import pytest
from app import app
from flask.testing import FlaskClient



@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert b'Home' in response.data
    assert response.status_code == 200


def test_login_page(client):
    response = client.get('/login')
    assert b'Login' in response.data
    assert response.status_code == 200

def test_register_page(client):
    response = client.get('/register')
    assert b'Register' in response.data
    assert response.status_code == 200




def test_predict_page(client):
    response = client.get('/predict')
    assert b'URL.</p>\n' in response.data
    assert response.status_code == 405


if __name__ == "__main__":
    pytest.main([__file__])
