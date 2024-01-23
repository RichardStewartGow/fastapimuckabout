from contextlib import AbstractContextManager
from typing import Callable, Iterator

from sqlalchemy.orm import Session

from app.domain.post_event import PostEvent
from app.domain.event import Event
from uuid import uuid4

class EventRepository:

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[Event]:
        with self.session_factory() as session:
            return session.query(Event).all()
        
    def add(self, incoming_input: PostEvent) -> Event:
        with self.session_factory() as session:
            event = Event(
                guid=str(uuid4()), dim_id_1=incoming_input.dim_id_1, dim_type_1=incoming_input.dim_type_1,
                dim_id_2=incoming_input.dim_id_2, dim_type_2=incoming_input.dim_type_2,
                dim_id_3=incoming_input.dim_id_3, dim_type_3=incoming_input.dim_type_3,
                ecategory=incoming_input.ecategory, etype=incoming_input.etype,
                especies=incoming_input.especies
            )
            session.add(event)
            session.commit()
            session.refresh(event)
            return event