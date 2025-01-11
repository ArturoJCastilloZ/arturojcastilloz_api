from app.database.connection import db, storage_bucket
from app.services.firebase_excepctions import handle_firebase_exception
from datetime import timedelta

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
    def fetch_images():
        """
        Obtiene las URL de descarga para múltiples imágenes desde Firebase Storage.
        
        * @param image_names: Lista de nombres de las imágenes a obtener
        * @returns: Lista de URLs de descarga de las imágenes
        """
        try:
            # Listar todos los archivos dentro del directorio 'assets/'
            blobs = storage_bucket.list_blobs(prefix='assets/')  # Prefix indica el directorio
            download_urls = []

            # Para cada archivo (blob) en el directorio, generamos su URL de descarga
            for blob in blobs:
                download_url = blob.generate_signed_url(expiration=timedelta(hours=1))  # URL firmada por 1 hora
                download_urls.append(download_url)

            return download_urls
        except Exception as e:
            print(f"Error al obtener las URL de descarga de las imágenes: {e}")
            return []

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