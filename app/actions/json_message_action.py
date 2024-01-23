from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.actions.action_interface import ActionInterface

class JsonMessageAction(ActionInterface):
    """
    return payload as a json response (reflection)
    """
    def run(self, payload: str) -> JSONResponse:
        return JSONResponse(
            content=jsonable_encoder({"msg": payload})
        )
