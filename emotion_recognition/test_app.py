from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_read_app():
    """_summary_
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, dear friend"}


def test_create_image_properties():
    """_summary
    """
