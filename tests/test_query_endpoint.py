
def test_no_query(test_app):
    response = test_app.get("/query/")
    assert response.status_code == 200
    assert response.json() == {"msg": "No query specified"}


def test_query_too_long(test_app):
    response = test_app.get("/query/?query=ladsladsladsladsladsladsladsladsladsladsladslads")
    assert response.status_code == 422

def test_hello_world(test_app):
    response = test_app.get("/query/?query=response&type=hello")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello world"}

def test_reverse(test_app):
    response = test_app.get("/query/?query=response&type=reverse&payload=racecarisracecasespeltbackwards")
    assert response.status_code == 200
    assert response.json() == {"msg": "sdrawkcabtlepsesacecarsiracecar"}
