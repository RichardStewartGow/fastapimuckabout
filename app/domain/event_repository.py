from contextlib import AbstractContextManager
from typing import Callable, Iterator

from sqlalchemy.orm import Session

from app.domain.event import Event

class EventRepository:

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[Event]:
        with self.session_factory() as session:
            return session.query(Event).all()
        
    def add(
            self, id: int, guid: str, 
            dim_id_1: int, dim_type_1: int, 
            dim_id_2: int, dim_type_2: int, 
            dim_id_3: int, dim_type_3: int,
            category: str, type: str,
            species: str
        ) -> Event:
        with self.session_factory() as session:
            event = Event(id=id, guid=guid, dim_id_1=dim_id_1)
            session.add(event)
            session.commit()
            session.refresh(event)
            return event