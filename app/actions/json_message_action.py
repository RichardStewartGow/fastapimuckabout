from typing import Annotated
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from .action_interface import ActionInterface

class JsonMessageAction(ActionInterface):
    def run(self, input: str) -> JSONResponse:
        return JSONResponse(
            content=jsonable_encoder({"msg": input})
        )