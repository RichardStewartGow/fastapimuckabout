"""
Apps di container, registers and providers actions, repos and services
"""
from dependency_injector import containers, providers

from app.actions import json_message_action, is_valid
from app.database import Database
from app.domain.event_repository import EventRepository
from app.domain.event_service import EventService
from app.config import Settings

settings = Settings()

db_url = f"{settings.db_engine}://{settings.db_user}:{settings.db_password}@{settings.db_host}"

class Container(containers.DeclarativeContainer):
    """
    Di container for app
    """
    wiring_config = containers.WiringConfiguration(modules=[".endpoints"])

    db = providers.Singleton(Database, db_url=db_url)

    json_message_action = providers.Callable(
        json_message_action.JsonMessageAction
    )

    is_valid = providers.Callable(
        is_valid.IsValid
    )

    event_repository = providers.Factory(
        EventRepository,
        session_factory=db.provided.session,
    )

    event_service = providers.Factory(
        EventService,
        event_repository=event_repository
    )
