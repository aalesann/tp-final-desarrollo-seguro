# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_USER = "root"
DB_PASSWORD = "example"
DB_HOST = "127.0.0.1"  # ⚠️ NO uses 'localhost' (en MySQL puede intentar socket)
DB_PORT = "3306"
DB_NAME = "chavela"

DATABASE_URL = (
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,      # revalida conexiones muertas
    pool_recycle=280,        # recicla conexiones para evitar TIME_WAIT
    connect_args={"connect_timeout": 5},  # timeout corto => falla rápido si no conecta
)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
