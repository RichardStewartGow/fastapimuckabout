from dependency_injector import containers, providers

from .actions import json_message_action

class Container(containers.DeclarativeContainer):
    """
    Di container for app
    """
    wiring_config = containers.WiringConfiguration(modules=[".endpoints"])

    json_message_action = providers.Callable(
        json_message_action.JsonMessageAction
    )
