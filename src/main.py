from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from src.config import Config
from src.controllers.http import dossier_router
from src.ioc import AppProvider

config = Config()
container = make_async_container(AppProvider(), context={Config: config})


def get_fastapi_app() -> FastAPI:
    fastapi_app = FastAPI()
    fastapi_app.include_router(dossier_router)

    setup_dishka(container, fastapi_app)

    return fastapi_app


def get_app():
    fastapi_app = get_fastapi_app()
    return fastapi_app
