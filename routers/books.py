# routers/books.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import create_book, get_books
from schemas import BookBase, BookResponse
from typing import List

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


@router.post("/", response_model=BookResponse)
def add_book(book: BookBase, db: Session = Depends(get_db)):
    # Ensure `create_book` returns a dict-like structure
    return create_book(db, book)


@router.get("/", response_model=List[BookResponse])
def list_books(db: Session = Depends(get_db)):
    # Ensure `get_books` returns a list of dict-like objects
    return get_books(db)
