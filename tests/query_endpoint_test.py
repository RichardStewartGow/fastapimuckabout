"""
tests for /query endpoint
"""
def test_no_query_get(test_app):
    """
    test error message when no query speficied
    """
    response = test_app.get("/query/")
    assert response.status_code == 200
    assert response.json() == {"msg": "No query specified"}


def test_query_too_long_get(test_app):
    """
    test against too long get lengths and response with 422
    """
    response = test_app.get("/query/?query=ladsladsladsladsladsladsladsladsladsladsladslads")
    assert response.status_code == 422

def test_hello_world_get(test_app):
    """
    can we load and get a good response from the hello world stategy
    """
    response = test_app.get("/query/?query=response&qtype=hello")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello world"}

def test_reverse_get(test_app):
    """
    can we load and get a good response from the reserve strategy
    """
    response = test_app.get(
        "/query/?query=response&qtype=reverse&payload=racecarisracecasespeltbackwards"
    )
    assert response.status_code == 200
    assert response.json() == {"msg": "sdrawkcabtlepsesacecarsiracecar"}


def test_validity_post_no_input(test_app):

    response = test_app.post(
        "/query/"
    )

    assert response.status_code == 422