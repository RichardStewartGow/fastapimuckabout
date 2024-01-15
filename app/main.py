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

@app.get("/query/")
async def run_query(
   q: Annotated[str | None, Query(max_length=50)] = None
):
    ##print(query)
    ##print(q)
    return {"test": q}
    