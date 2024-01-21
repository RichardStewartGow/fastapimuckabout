from typing import Annotated
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

def run(input_string: str) -> JSONResponse:
    return JSONResponse(
        content=jsonable_encoder({"msg": input_string})
    )