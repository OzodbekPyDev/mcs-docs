from contextlib import asynccontextmanager

from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.v1 import all_routers
from app.infrastructure.config import settings
from app.infrastructure.di.providers.adapters import AdaptersProvider
from app.infrastructure.di.providers.db import DBProvider
from app.infrastructure.di.providers.interactors.files import \
    FilesInteractorProvider
from app.infrastructure.di.providers.repositories import RepositoriesProvider
from app.infrastructure.exception_handlers import init_exception_handlers


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await app.state.dishka_container.close()


app = FastAPI(title="KIUT DOCS MICROSERVICE", lifespan=lifespan)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/app/media", StaticFiles(directory="./app/media"), name="media")

for router in all_routers:
    app.include_router(router, prefix=settings.api_prefix)

container = make_async_container(
    DBProvider(),
    AdaptersProvider(),
    RepositoriesProvider(),
    FilesInteractorProvider(),
)
setup_dishka(container, app)

init_exception_handlers(app)
