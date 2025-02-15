import firebase_admin
from firebase_admin import credentials, firestore, storage
from .configuration import Settings

def initialize_firebase():
    """
    Inicializa la conexión con FIrebase y retorna una instancia del cliente Firestore.

    * @function initialize_firebase
    * @returns {firestore.Client} Instancia del cliente de Firestore
    * @throws {FirebaseError} Si hay un error en la inicialización
    """
    try:
        # Se obtenien las credenciales para la conexión
        cred = credentials.Certificate(Settings.get_firebase_credentials())
        # Se inicializa la aplicacion con Firebase
        firebase_admin.initialize_app(cred, {
            'databaseURL': Settings.get_database_url(),
            'storageBucket': Settings.get_storage_bucket()
        })
        
        # Se crea el cliente de Firestore
        db = firestore.client()
        
        bucket = storage.bucket()
        return db, bucket
    except Exception as e:
        raise Exception(f"Error al inicializar Firebase: {str(e)}")

# Crear una instancia global de la base de datos
db, storage_bucket = initialize_firebase()