from fastapi import FastAPI

from app.api.endpoints import v1_router
from app.config import settings

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(v1_router)
