from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_working():
    response = client.get("/")
    assert response.status_code == 200


def test_url_predict():
    response = client.post("/predict_breed/",
                           json={"link": "https://www.ellevetsciences.com/wp-content/uploads/2022/09/ev-blog-scottishfold_header-1024x683.jpg"})
    json_data = response.json()

    assert response.status_code == 200
    assert json_data['breed'] == 'Шотландская вислоухая'


def test_not_url_predict():
    response = client.post("/predict_breed/",
                           json={"link": "not_an_url"})
    json_data = response.json()
    assert json_data['error'] == 'Invalid link'
