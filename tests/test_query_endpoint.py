def test_hello_world(test_app):
    response = test_app.get("/query/?q=Hello")
    assert response.status_code == 200
    assert response.json() == {"test": "Hello"}