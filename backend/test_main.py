from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_pear():
    response = client.post("/fruits", json={"name": "pear"})
    assert response.status_code == 200
    assert response.json() == {"name": "pear"}

    response = client.get("/fruits")
    assert response.status_code == 200
    assert response.json() == {"fruits": [{"name": "pear"}]}