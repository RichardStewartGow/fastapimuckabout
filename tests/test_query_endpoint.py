
def test_no_query(test_app):
    response = test_app.get("/query/")
    assert response.status_code == 200
    assert response.json() == {"msg": "No query specified"}

def test_hello_world(test_app):
    response = test_app.get("/query/?query=test")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello"}