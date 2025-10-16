from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from auth import admin_required
from schemas import UserCreate, UserUpdate, UserOut
from crud.users import create_user, list_users, get_user, update_user, delete_user
from models import Role

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[UserOut])
def _list_users(_: None = Depends(admin_required), db: Session = Depends(get_db)):
    return list_users(db)

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def _create_user(data: UserCreate, _: None = Depends(admin_required), db: Session = Depends(get_db)):
    try:
        return create_user(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=UserOut)
def _get_user(user_id: int, _: None = Depends(admin_required), db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="No encontrado")
    return user

@router.patch("/{user_id}", response_model=UserOut)
def _update_user(user_id: int, data: UserUpdate, _: None = Depends(admin_required), db: Session = Depends(get_db)):
    try:
        return update_user(db, user_id, data)
    except LookupError:
        raise HTTPException(status_code=404, detail="No encontrado")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def _delete_user(user_id: int, _: None = Depends(admin_required), db: Session = Depends(get_db)):
    try:
        delete_user(db, user_id)
    except LookupError:
        raise HTTPException(status_code=404, detail="No encontrado")
