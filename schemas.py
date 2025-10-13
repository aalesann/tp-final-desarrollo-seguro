from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List


class RolOut(BaseModel):
    id: int
    codigo: str
    nombre: str

    class Config:
        orm_mode = True


class UsuarioOut(BaseModel):
    id: str
    nombre_usuario: str
    nombre_completo: str
    correo_electronico: EmailStr
    activo: bool
    roles: Optional[List[RolOut]] = []

    class Config:
        orm_mode = True


class UsuarioCreate(BaseModel):
    nombre_usuario: str
    nombre_completo: str
    correo_electronico: EmailStr
    activo: Optional[bool] = True
