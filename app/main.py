from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router import app_router
from app.utils.tags import TAGS_METADATA

origins = [
    "http://localhost:4200",
]

app = FastAPI(
    title="ArturoJCastilloZ API",
    description="Api para obtener mis datos de Firebase",
    version="1.0.0",
    openapi_tags=TAGS_METADATA,
    swagger_ui_parameters={ "docExpansion": "none" }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Orígenes permitidos
    allow_credentials=True,  # Permitir envío de cookies/autenticación
    allow_methods=["*"],  # Métodos permitidos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Encabezados permitidos
)

app.include_router(app_router.router, prefix="/api");
