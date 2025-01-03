import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def get_firebase_credentials():
        credentials = {
            "type": os.getenv("TYPE"),
            "project_id": os.getenv("PROJECT_ID"),
            "private_key_id": os.getenv("PRIVATE_KEY_ID"),
            "private_key": os.getenv("PRIVATE_KEY").replace(r"\n", "\n"),
            "client_email": os.getenv("CLIENT_EMAIL"),
            "client_id": os.getenv("CLIENT_ID"),
            "auth_uri": os.getenv("AUTH_URI"),
            "token_uri": os.getenv("TOKEN_URI"),
            "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER"),
            "client_x509_cert_url": os.getenv("CLIENT"),
            "universe_domain": os.getenv("DOMAIN")
        }
        return credentials
    
    def get_database_url():
        url = os.getenv("URL")
        return url