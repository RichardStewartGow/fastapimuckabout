from dependency_injector import containers, providers

from .actions import json_message_action, is_valid
from .database import Database

from app.config import Settings

settings = Settings()

SQLALCHEMY_DATABASE_URL = f"{settings.db_engine}://{settings.db_user}:{settings.db_password}@{settings.db_host}"

class Container(containers.DeclarativeContainer):
    """
    Di container for app
    """
    wiring_config = containers.WiringConfiguration(modules=[".endpoints"])

    db = providers.Singleton(Database, db_url=SQLALCHEMY_DATABASE_URL)

    json_message_action = providers.Callable(
        json_message_action.JsonMessageAction
    )

    is_valid = providers.Callable(
        is_valid.IsValid
    )
