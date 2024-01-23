"""
Mocked unit tests for db endpoints
"""
from unittest import mock
from fastapi.testclient import TestClient
from app.domain.event_repository import EventRepository
from app.domain.event import Event

def test_get_event_list(test_app):
    repository_mock = mock.Mock(spec=EventRepository)
    repository_mock.get_all.return_value = [
        'test'
    ]

    with test_app.container.event_repository.override(repository_mock):
        response = test_app.get('/events')