import pytest
from app import app

def test_general_page():
    response = app.test_client().get('/')
    assert response.status_code == 200