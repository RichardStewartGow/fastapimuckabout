"""
Routes
"""
from typing import Annotated, Union

from fastapi import APIRouter, Query, Depends, status
from dependency_injector.wiring import inject, Provide
from app.factories import abstract_factory
from app.containers import Container
from app.domain.post_query import PostQuery
from app.domain.post_event import PostEvent
from app.domain.event_service import EventService

from .actions import json_message_action

router = APIRouter()


@router.get("/readyz")
@inject
async def ready(
    jmsgaction: json_message_action = Depends(Provide[Container.json_message_action])
):
    """
    k8 ready endpoint
    """
    return jmsgaction.run("OK")


@router.get("/healthz")
@inject
async def health(
    jmsgaction: json_message_action = Depends(Provide[Container.json_message_action])
):
    """
    k8 health endpoint
    """
    ## @TODO needs to actually assert health, quick query probs.
    return jmsgaction.run("OK")


@router.get("/query/")
@inject
async def run_query_get(
    query: Annotated[Union[str,None], Query(max_length=30)] = None,
    qtype:  Annotated[Union[str,None], Query(max_length=30)] = None,
    payload: Annotated[Union[str,None], Query(max_length=50)] = None,
    jmsgaction: json_message_action = Depends(Provide[Container.json_message_action])
):
    """
    Main query endpoint, calls a series of constructors based off hierachical prarams

    query (str): the type of query top level categorisation, organisationn level for the strategies
    type (str): the spesific type of strategy to run 
    payload (str): if appropriate the payload workload for the strategy to operate on

    make the abstract load the target strategy class, 
    then run with payload or not
    """

    if query is None:
        return jmsgaction.run("No query specified")
    if qtype is None:
        return jmsgaction.run("No query type specified")
    if payload:
        return abstract_factory.get_factory(query, qtype, payload)().run(payload)

    return abstract_factory.get_factory(query, qtype, payload)().run()


@router.post("/query/")
async def run_query_post(
    query: PostQuery
):
    return abstract_factory.get_factory(query.query, query.qtype, query.payload)().run(query.payload)

@router.get(
   "/events",     
)
@inject
async def get_all(
    event_service: EventService = Depends(Provide[Container.event_service])
):
    """
    Return all events
    """
    return event_service.get_events()


@router.post(
    "/events",
    status_code=status.HTTP_204_NO_CONTENT,
)
@inject
async def create_event(
    incoming_event: PostEvent,
    event_service: EventService = Depends(Provide[Container.event_service])
):
    print('test')

    """
    Bit articial atm, you'd want to pass dimensions at the same time relevant to the event and do mutliple
    writes
    """
    return event_service.add_event(incoming_event)