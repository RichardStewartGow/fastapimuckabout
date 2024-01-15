from typing import Annotated

from fastapi import FastAPI, Path, Query
from app.factories import abstract_factory

app = FastAPI()

@app.get("/readyz")
async def ready():
    return {"msg": "OK"}

@app.get("/healthz")
async def health():
    ## @TODO needs to actually assert health, quick query probs.
    return {"msg": "OK"}

@app.get("/query/{target}")
async def run_query(
    query: Annotated[int, Path(title="The Query to run")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    print(query)
    print(q)
    return {"test": "yes"}
    