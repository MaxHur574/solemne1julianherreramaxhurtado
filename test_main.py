from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_chile_time():
    response = client.get("/time")
    assert response.status_code == 200

    data = response.json()
    assert "hora_actual_chile" in data
    assert isinstance(data["hora_actual_chile"], str)
    assert len(data["hora_actual_chile"]) > 0
