"""
test k8 endpoints
"""

def test_ready(test_app):
    """
    test k8 ready endpoint
    """
    response = test_app.get("/readyz")
    assert response.status_code == 200
    assert response.json() == {"msg": "OK"}

def test_healthy(test_app):
    """
    test k8s health endpoint
    """
    response = test_app.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"msg": "OK"}
    