def test_hello_world(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}