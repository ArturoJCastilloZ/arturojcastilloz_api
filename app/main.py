from fastapi import FastAPI
from app.router import app_router

app = FastAPI(
    title="ArturoJCastilloZ API",
    description="Api para obtener mis datos de Firebase",
    version="1.0.0",
)

app.include_router(app_router.router, prefix="/api");
