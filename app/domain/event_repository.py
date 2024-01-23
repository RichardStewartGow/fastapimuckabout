from contextlib import AbstractContextManager
from typing import Callable, Iterator

from sqlalchemy.orm import Session

from app.domain.post_event import PostEvent
from app.domain.event import Event

class EventRepository:

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[Event]:
        with self.session_factory() as session:
            return session.query(Event).all()
        
    def add(self, input: PostEvent) -> Event:
        with self.session_factory() as session:
            event = Event(input)
            session.add(event)
            session.commit()
            session.refresh(event)
            return event