from fastapi import APIRouter
from app.services.firebase_services import FirebaseServices 

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Bienvenido a Firebase API"}

@router.get("/about")
async def About_Section():
    return FirebaseServices.get_about_section()

@router.get("/header")
async def Header_Section():
    return FirebaseServices.get_headers_section()

@router.get("/hero")
async def Hero_Section():
    return FirebaseServices.get_hero_section()

@router.get("/jobs")
async def Jobs_Section():
    return FirebaseServices.get_jobs_section()

@router.get("/skills")
async def Skills_Section():
    return FirebaseServices.get_skills_section()

@router.get("/social")
async def Social_Section():
    return FirebaseServices.get_social_section()

@router.get("/studies")
async def Studies_Section():
    return FirebaseServices.get_studies_section()