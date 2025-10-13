from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from secrets import compare_digest

security = HTTPBasic()

# Credenciales simuladas (más adelante lo conectamos a la BD)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "example"

def autenticar(credentials: HTTPBasicCredentials = Depends(security)):
    correct_user = compare_digest(credentials.username, ADMIN_USERNAME)
    correct_pass = compare_digest(credentials.password, ADMIN_PASSWORD)

    if not (correct_user and correct_pass):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
