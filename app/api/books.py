from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db import crud

from app.schemas import (
    BookCreate,
    BookResponse
)

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


@router.get(
    "/",
    response_model=list[BookResponse]
)
def get_books(
    category_id: int | None = None,
    db: Session = Depends(get_db)
):
    books = crud.get_books(db)

    if category_id:
        books = [
            book
            for book in books
            if book.category_id == category_id
        ]

    return books


@router.get(
    "/{book_id}",
    response_model=BookResponse
)
def get_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    book = crud.get_book(
        db,
        book_id
    )

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book


@router.post(
    "/",
    response_model=BookResponse,
    status_code=201
)
def create_book(
    book: BookCreate,
    db: Session = Depends(get_db)
):
    category = crud.get_category(
        db,
        book.category_id
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return crud.create_book(
        db,
        book.title,
        book.description,
        book.price,
        book.url,
        book.category_id
    )