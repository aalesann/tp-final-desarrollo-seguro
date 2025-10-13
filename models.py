from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Enum, BigInteger
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base
import enum
import uuid


class RolCodigo(enum.Enum):
    administrador = "administrador"
    tecnico = "tecnico"
    recepcionista = "recepcionista"


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre_usuario = Column(String(100), unique=True, nullable=False)
    nombre_completo = Column(String(150), nullable=False)
    correo_electronico = Column(String(150), unique=True, nullable=False)
    activo = Column(Boolean, default=True)
    creado_el = Column(DateTime, default=datetime.utcnow)
    actualizado_el = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    roles = relationship("UsuarioRol", back_populates="usuario")


class Rol(Base):
    __tablename__ = "roles"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    codigo = Column(Enum(RolCodigo), unique=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    creado_el = Column(DateTime, default=datetime.utcnow)
    actualizado_el = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    usuarios = relationship("UsuarioRol", back_populates="rol")


class UsuarioRol(Base):
    __tablename__ = "usuarios_roles"

    usuario_id = Column(CHAR(36), ForeignKey("usuarios.id"), primary_key=True)
    rol_id = Column(BigInteger, ForeignKey("roles.id"), primary_key=True)
    asignado_el = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario", back_populates="roles")
    rol = relationship("Rol", back_populates="usuarios")
