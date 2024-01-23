from typing import Iterator
from app.domain.event import Event
from app.domain.event_repository import EventRepository
from app.domain.post_event import PostEvent


class EventService:
    def __init__(self, event_repository: EventRepository) -> None:
        self._repository: EventRepository = event_repository


    def get_events(self) -> Iterator[Event]:
        return self._repository.get_all()
    
    def add_event(self, input: PostEvent) -> Event:
        return self._repository.add(input)