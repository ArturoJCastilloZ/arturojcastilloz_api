from fastapi import HTTPException
from firebase_admin import firestore

class FirebaseError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=500, detail=detail)

def handle_firebase_exception(e: Exception) -> list:
    if isinstance(e, firestore.exceptions.NotFound):
        print(f"Colección no encontrada: {str(e)}")
        return []
    elif isinstance(e, firestore.exceptions.PermissionDenied):
        print(f"Error de permisos: {str(e)}")
        raise FirebaseError(detail="Error de permisos al acceder a la colección")
    elif isinstance(e, firestore.exceptions.ServiceUnavailable):
        print(f"Servicio no disponible: {str(e)}")
        raise FirebaseError(detail="Servicio de Firestore no disponible")
    else:
        print(f"Error inesperado: {str(e)}")
        raise FirebaseError(detail=f"Error al obtener la información: {str(e)}")