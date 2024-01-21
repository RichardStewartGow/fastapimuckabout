from typing import Annotated
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.actions.action_interface import ActionInterface

class JsonMessageAction(ActionInterface):
    def run(self, payload: str) -> JSONResponse:
        return JSONResponse(
            content=jsonable_encoder({"msg": payload})
        )