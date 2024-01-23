"""
Mocked unit tests for db endpoints
"""
from unittest import mock
from uuid import uuid4
from fastapi.testclient import TestClient
from app.domain.event_repository import EventRepository
from app.domain.event import Event
from app.application import app

def test_get_event_list(test_app):
    repository_mock = mock.Mock(spec=EventRepository)
    repository_mock.get_all.return_value = [
        Event(id=1, guid=uuid4(), dim_id_1=1, dim_type_1='USER', dim_id_2=1, dim_type_2='POST', ecategory="COMMUNICATION", etype='CREATION', especies='MESSAGE_POST'),
        Event(id=2, guid=uuid4(), dim_id_1=1, dim_type_1='USER', dim_id_2=2, dim_type_2='USER', dim_id_3=1, dim_type_3='POST', ecategory="COMMUNICATION", etype='CREATION', especies='MESSAGE_LIKE'),
    ]

    with app.container.event_repository.override(repository_mock):
        response = test_app.get('/events')

        assert response.status_code == 200
        data = response.json()
        print(data)
