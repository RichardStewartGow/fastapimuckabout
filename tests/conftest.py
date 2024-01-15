import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

def start_application():
    app = FastAPI()
    return app