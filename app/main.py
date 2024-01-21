from typing import Annotated, Union

from fastapi import FastAPI, Query
from app.factories import abstract_factory
from app.actions.json_message_action import run as json_make

app = FastAPI()

"""
k8 ready endpoint
"""
@app.get("/readyz")
async def ready():
    return {"msg": "OK"}

"""
k8 health endpoint
"""
@app.get("/healthz")
async def health():
    ## @TODO needs to actually assert health, quick query probs.
    return {"msg": "OK"}

"""
Main query enndpoint, calls a series of constructors based off hierachical prarams

query (str): the type of query, 
"""
@app.get("/query/")
async def run_query(
   query: Annotated[Union[str,None], Query(max_length=30)] = None,
   type:  Annotated[Union[str,None], Query(max_length=30)] = None,
   payload: Annotated[Union[str,None], Query(max_length=50)] = None
):
    if query is None:
       return json_make("No query specified")
    
    if type is None:
        return json_make("No query type specified")

    return abstract_factory.get_factory(query, type, payload)

    