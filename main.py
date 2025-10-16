from fastapi import FastAPI, Depends
from database import SessionLocal
from models import Usuario, Rol
from schemas import UsuarioOut, RolOut
from auth import autenticar

app = FastAPI(title="API REST (FastAPI + MySQL)")

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/auth/health")
def auth_health(user=Depends(autenticar)):
    return {"ok": True, "who": user}

#! TODO: Modularizar sesión
# Dependencia para obtener una sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", tags=["Inicio"])
def index(usuario: str = Depends(autenticar)):
    return {"mensaje": f"Bienvenido {usuario}. Autenticación correcta."}

@app.get("/usuarios", response_model=list[UsuarioOut], tags=["Usuarios"])
def listar_usuarios(db=Depends(get_db), usuario: str = Depends(autenticar)):
    return db.query(Usuario).all()

@app.get("/roles", response_model=list[RolOut], tags=["Roles"])
def listar_roles(db=Depends(get_db), usuario: str = Depends(autenticar)):
    return db.query(Rol).all()
