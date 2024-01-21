from dependency_injector import containers, providers

from .actions import json_message_action

class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[".endpoints"])

    #config = providers.Configuration(yaml_files=["config.yml"])

    json_message_action = providers.Callable(
        json_message_action.JsonMessageAction
    )