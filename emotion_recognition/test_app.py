from fastapi.testclient import TestClient
from emotion_recognition.app import app

client = TestClient(app)


def test_read_app():
    """_summary_
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, dear friend"}


def test_pay_attention():
    """
    _summary_
    """
    response = client.get("/attetion")
    assert response.status_code == 200
    assert response.json() == {"message": "See ResNet50 Class List on"
                               "deeplearning.cms.waikato.ac.nz"}
