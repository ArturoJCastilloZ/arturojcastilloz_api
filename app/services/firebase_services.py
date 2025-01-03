from app.database.connection import db
from app.services.firebase_excepctions import handle_firebase_exception

class FirebaseServices():
    @staticmethod
    def get_collection_name(collection_name: str):
        try:
            print(f"Intentando obtener colección: {collection_name}")
            ref = db.collection(collection_name).get()
            print(f"Referencia obtenida para {collection_name}: {ref}")
            
            if not ref:
                print(f"La colección {collection_name} está vacía")
                return []
                
            documents = [data.to_dict() for data in ref]
            print(f"Documentos encontrados en {collection_name}: {len(documents)}")
            return documents
        except Exception as e:
            return handle_firebase_exception(e)

    @staticmethod
    def get_hero_section():
        return FirebaseServices.get_collection_name("hero")

    @staticmethod
    def get_about_section():
        return FirebaseServices.get_collection_name("about")

    @staticmethod
    def get_headers_section():
        return FirebaseServices.get_collection_name("header")

    @staticmethod
    def get_jobs_section():
        return FirebaseServices.get_collection_name("jobs")

    @staticmethod
    def get_skills_section():
        return FirebaseServices.get_collection_name("skills")

    @staticmethod
    def get_social_section():
        return FirebaseServices.get_collection_name("social")

    @staticmethod
    def get_studies_section():
        return FirebaseServices.get_collection_name("studies")