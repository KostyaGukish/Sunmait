from fastapi.testclient import TestClient
from service import app, TextInput

client = TestClient(app)


class TestEndpoints:
    def test_ping_endpoint(self):
        response = client.get("/ping")
        assert response.status_code == 200
        assert response.json() == {"status": "OK"}

    def test_predict_endpoint_with_valid_input(self):
        input_data = TextInput(text="This is a test text for summarization.")
        response = client.post("/predict", json=input_data.model_dump())
        assert response.status_code == 200
        assert "prediction" in response.json()
        assert isinstance(response.json()["prediction"], dict)

    def test_predict_endpoint_with_invalid_input(self):
        response = client.post("/predict", json={"invalid_field": "This is invalid"})
        assert response.status_code == 422
