"""
Mocked unit tests for db endpoints
"""
from unittest import mock
from fastapi.testclient import TestClient
from app.domain.event_repository import EventRepository
from app.domain.event import Event
from app.application import app

def test_get_event_list(test_app):
    repository_mock = mock.Mock(spec=EventRepository)
    repository_mock.get_all.return_value = [
        'test'
    ]

    with app.container.event_repository.override(repository_mock):
        response = test_app.get('/events')

        assert response.status_code == 200
        data = response.json()
        print(data)
