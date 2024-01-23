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
    """
    If we fire nothing at a post enndpoint expect 422
    """
    response = test_app.post(
        "/query/"
    )

    assert response.status_code == 422

def test_validity_post_bad_input(test_app):
    """
    if we fire a no PostQuery object 422 also
    """
    response = test_app.post(
        "/query/",
         json={
            "beep": "boop"
        }
    )

    assert response.status_code == 422




def test_validity_post_one_call(test_app):
    """
    Test the logical concept of validity, truth iff the conclusion cannot be false and the premise true
    where p = premise, q = conclusion
    """
    response = test_app.post(
        "/query/",
        json={
            "query": "response",
            "qtype": "valid",
            "payload": {
                "p": True,
                "q": False
            }
        }
    )

    assert response.status_code == 200
    assert response.json() == {"msg": "True => False is Not Valid"}

def test_validity_post_full_truth_table(test_app):
    """
    map/test the entire truth table my using the zip iterator to iterate over 3 dicts as once
    """
    truth_table_inputs_p = {
            "p1": True,
            "p2": True,
            "p3": False,
            "p4": False,
    }

    truth_table_inputs_q = {
            "q1": True,
            "q2": False,
            "q3": True,
            "q4": False,
    }

    truth_table_result = {
            1: "True => True is Valid",
            2: "True => False is Not Valid",
            3: "False => True is Valid",
            4: "False => False is Valid"
    }

    for k1, k2, k3 in zip(truth_table_inputs_p, truth_table_inputs_q, truth_table_result):
        response = test_app.post(
            "/query/",
            json={
                "query": "response",
                "qtype": "valid",
                "payload": {
                    "p": truth_table_inputs_p[k1],
                    "q": truth_table_inputs_q[k2]
                }
            }
        )

        assert response.status_code == 200
        assert response.json() == {"msg": truth_table_result[k3]}