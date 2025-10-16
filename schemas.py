from pydantic import BaseModel, Field

class RoleOut(BaseModel):
    id: int
    name: str
    class Config:
        from_attributes = True

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=100)
    is_active: bool = True
    role_id: int

class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

class UserUpdate(BaseModel):
    username: str | None = None
    password: str | None = None
    is_active: bool | None = None
    role_id: int | None = None

class UserOut(BaseModel):
    id: int
    username: str
    is_active: bool
    role: RoleOut
    class Config:
        from_attributes = True
