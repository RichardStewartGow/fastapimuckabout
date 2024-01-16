from typing import Annotated, Union

from fastapi import FastAPI, Path, Query
from app.factories import abstract_factory
from app.actions.json_message_action import run as json_make

app = FastAPI()

@app.get("/readyz")
async def ready():
    return {"msg": "OK"}

@app.get("/healthz")
async def health():
    ## @TODO needs to actually assert health, quick query probs.
    return {"msg": "OK"}

@app.get("/query/")
async def run_query(
   query: Annotated[Union[str,None], Query(max_length=30)] = None
):
    if query is None:
       return json_make("No query specified")

    return abstract_factory.get_factory(query)

    