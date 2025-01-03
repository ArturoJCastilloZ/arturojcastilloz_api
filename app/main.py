from fastapi import FastAPI
from app.router import app_router
from app.utils.tags import TAGS_METADATA

app = FastAPI(
    title="ArturoJCastilloZ API",
    description="Api para obtener mis datos de Firebase",
    version="1.0.0",
    openapi_tags=TAGS_METADATA,
    swagger_ui_parameters={ "docExpansion": "none" }
)

app.include_router(app_router.router, prefix="/api");
