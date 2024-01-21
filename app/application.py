"""Application module."""

from fastapi import FastAPI

from app.containers import Container
from app import endpoints


def create_app() -> FastAPI:
    """init fast api"""
    container = Container()

    fastapiapp = FastAPI()
    fastapiapp.container = container
    fastapiapp.include_router(endpoints.router)
    return fastapiapp


app = create_app()
