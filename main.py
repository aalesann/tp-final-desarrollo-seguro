from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import Role, User
from routers import users as users_router
from auth import get_password_hash
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    ADMIN_USER: str = "admin"
    ADMIN_PASSWORD: str = "example"

    class Config:
        env_file = ".env"
        extra = "ignore"

@lru_cache
def get_settings():
    return Settings()

app = FastAPI(title="MicroNova API - 1ra Entrega")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)  # crea tablas si no existen

@app.on_event("startup")
def seed_data():
    settings = get_settings()
    with next(get_db()) as db:  # abre sesión corta
        # crear roles si no existen
        for name in ["admin", "tecnica", "recepcionista"]:
            if not db.query(Role).filter(Role.name == name).first():
                db.add(Role(name=name))
        db.commit()
        # crear admin si no existe
        admin_role = db.query(Role).filter(Role.name == "admin").first()
        if not db.query(User).filter(User.username == settings.ADMIN_USER).first():
            db.add(
                User(
                    username=settings.ADMIN_USER,
                    password_hash=get_password_hash(settings.ADMIN_PASSWORD),
                    is_active=True,
                    role_id=admin_role.id,
                )
            )
            db.commit()

@app.get("/health")
def health():
    return {"status": "ok"}

# Router de usuarios (protegido por admin en el propio router)
app.include_router(users_router.router)
