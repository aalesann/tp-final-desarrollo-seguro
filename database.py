from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from pydantic_settings import BaseSettings
from functools import lru_cache
import os

class Settings(BaseSettings):
    DB_URL: str = "mysql+pymysql://root:root@localhost:3306/micronova"

    class Config:
        env_file = ".env"
        extra = "ignore"

@lru_cache
def get_settings():
    return Settings()

settings = get_settings()

engine = create_engine(settings.DB_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

# dependencia por request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
