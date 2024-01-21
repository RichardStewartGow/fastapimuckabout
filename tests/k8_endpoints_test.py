def test_ready(test_app):
    response = test_app.get("/readyz")
    assert response.status_code == 200
    assert response.json() == {"msg": "OK"}

def test_healthy(test_app):
    response = test_app.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"msg": "OK"}