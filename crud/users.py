from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import User, Role
from schemas import UserCreate, UserUpdate
from auth import get_password_hash

def create_user(db: Session, data: UserCreate) -> User:
    user = User(
        username=data.username,
        password_hash=get_password_hash(data.password),
        is_active=data.is_active,
        role_id=data.role_id,
    )
    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("username ya existe")
    db.refresh(user)
    return user

def list_users(db: Session) -> list[User]:
    return db.query(User).all()

def get_user(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user_id: int, data: UserUpdate) -> User:
    user = get_user(db, user_id)
    if not user:
        raise LookupError("Usuario no encontrado")
    if data.username is not None:
        user.username = data.username
    if data.password is not None:
        user.password_hash = get_password_hash(data.password)
    if data.is_active is not None:
        user.is_active = data.is_active
    if data.role_id is not None:
        # validar rol existente
        role = db.query(Role).filter(Role.id == data.role_id).first()
        if not role:
            raise ValueError("Rol inválido")
        user.role_id = data.role_id
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("username ya existe")
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int) -> None:
    user = get_user(db, user_id)
    if not user:
        raise LookupError("Usuario no encontrado")
    db.delete(user)
    db.commit()
