
"""
pytest config and wireup
"""
import pytest
from starlette.testclient import TestClient

from app.application import app


#@todo need to refresh db for tests

@pytest.fixture(scope="module")
def test_app():
    """
    create a test client instance for consumption by tests
    """
    client = TestClient(app)
    yield client
