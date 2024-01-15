from typing import Generator
from typing import Any

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient


def start_application():
    app = FastAPI()
    return app

@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:

    _app = start_application()
    yield _app

@pytest.fixture(scope="function")
def client(
        app: FastAPI
) -> Generator[TestClient, Any, None]:
    with TestClient(app) as client:
        yield client
