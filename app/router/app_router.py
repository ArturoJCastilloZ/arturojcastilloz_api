from fastapi import APIRouter, Depends
from app.auth.auth import validate_api_key
from app.services.firebase_services import FirebaseServices 

router = APIRouter()

@router.get("/", tags=["Default"])
async def root():
    return {"message": "Bienvenido a Firebase API"}

@router.get(
    "/about", 
    tags=["About"],
    description="Obtiene un arreglo una breve descripción sobre mi."
)
async def About_Section():
    return FirebaseServices.get_about_section()

@router.get(
    "/header",
    tags=["Header"],
    description="Se obtiene una lista de opciones que se muestran en el encabezado\
        y también sus enlaces."
)
async def Header_Section():
    return FirebaseServices.get_headers_section()

@router.get(
    "/hero",
    tags=["Hero"],
    description="Listado de información principal del siito."
)
async def Hero_Section():
    return FirebaseServices.get_hero_section()

@router.get(
    "/jobs",
    tags=["Jobs"],
    description="Listado de empleos que he tenido, así como una descripción de mis actividad y duración."
)
async def Jobs_Section():
    return FirebaseServices.get_jobs_section()

@router.get(
    "/skills",
    tags=["Skills"],
    description="Listado de habilidad que he adquirido en mi trayectoria profesional."
)
async def Skills_Section():
    return FirebaseServices.get_skills_section()

@router.get(
    "/social",
    tags=["Social"],
    description="Listado de mis redes sociales con iconos, url y un titulo. Entre otra información, pero esa es la importante"
)
async def Social_Section():
    return FirebaseServices.get_social_section()

@router.get(
    "/studies",
    tags=["Studies"],
    description="Se obtiene un listado con mi trayectoria estudiantil universitaria."
)
async def Studies_Section():
    return FirebaseServices.get_studies_section()