# routers/users.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import create_user, get_users
from schemas import UserCreate, UserResponse
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/", response_model=UserResponse)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.get("/", response_model=List[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return get_users(db)


# update routers/users.py

# @router.post("/", response_model=UserResponse)
# def add_user(user: UserCreate, db: Session = Depends(get_db)):
#     existing_user = db.query(User).filter(User.email == user.email).first()
#     if existing_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return create_user(db, user)
