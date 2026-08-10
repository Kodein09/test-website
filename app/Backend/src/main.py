from fastapi import FastAPI

from .core.config import settings
from .routers import auth_router

async def lifespan(app: FastAPI):
    settings.database_url()

app = FastAPI(title="Welcome to DiceHub", lifespan=lifespan)

app.include_router(auth_router.router)
