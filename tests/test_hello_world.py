def test_hello_world(client):
    response = client.get("/")
    assert response.json()['msg'] == "Hello world"