from typing import Annotated, Union

from fastapi import APIRouter, Query, Depends
from app.factories import abstract_factory
from dependency_injector.wiring import inject, Provide
from .containers import Container

from .actions import json_message_action

router = APIRouter()

"""
k8 ready endpoint
"""
@router.get("/readyz")
@inject
async def ready(
    json_message_action: json_message_action = Depends(Provide[Container.json_message_action])
):
    return json_message_action.run("OK")

"""
k8 health endpoint
"""
@router.get("/healthz")
@inject
async def health(
    json_message_action: json_message_action = Depends(Provide[Container.json_message_action])
):
    ## @TODO needs to actually assert health, quick query probs.
    return json_message_action.run("OK")

"""
Main query enndpoint, calls a series of constructors based off hierachical prarams

query (str): the type of query top level categorisation, organisationn level for the strategies
type (str): the spesific type of strategy to run 
payload (str): if appropriate the payload workload for the strategy to operate on
"""
@router.get("/query/")
@inject
async def run_query(
    query: Annotated[Union[str,None], Query(max_length=30)] = None,
    type:  Annotated[Union[str,None], Query(max_length=30)] = None,
    payload: Annotated[Union[str,None], Query(max_length=50)] = None,
    json_message_action: json_message_action = Depends(Provide[Container.json_message_action])
):
    if query is None:
       return json_message_action.run("No query specified")
    
    if type is None:
        return json_message_action.run("No query type specified")

    return abstract_factory.get_factory(query, type, payload)

    