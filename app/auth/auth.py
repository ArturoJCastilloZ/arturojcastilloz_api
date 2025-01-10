from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

# Ruta para obtener el token (puedes cambiarla si tienes otra configuración)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Clave secreta para firmar el token (mantén esto seguro y privado)
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

from datetime import datetime, timedelta
from jose import jwt

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    print(encoded_jwt)
    return encoded_jwt

# Función para validar el token
def verify_token(token: str = Depends(oauth2_scheme)):
    print(create_access_token())
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  # Retorna el contenido del token
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )