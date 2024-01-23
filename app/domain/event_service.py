from app.domain.event import Event
from app.domain.event_repository import EventRepository
from typing import Iterator

class EventService:
    def __init__(self, event_repository: EventRepository) -> None:
        self._repository: EventRepository = event_repository


    def get_events(self) -> Iterator[Event]:
        return self._repository.get_all()