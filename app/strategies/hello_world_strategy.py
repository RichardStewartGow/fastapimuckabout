#from app.actions.json_message_action import run as json_make
from fastapi import Depends
from app.containers import Container
from app.actions import json_message_action
from dependency_injector.wiring import inject, Provide

@inject
def run(
    json_message_action: json_message_action = Depends(Provide[Container.json_message_action])
):
    return json_message_action.run("Hello world")