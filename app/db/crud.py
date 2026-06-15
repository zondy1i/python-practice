from app.db.models import Category
from app.db.models import Book


# CATEGORY CRUD

def create_category(db, title):
    category = Category(title=title)

    db.add(category)
    db.commit()
    db.refresh(category)

    return category


def get_categories(db):
    return db.query(Category).all()


# BOOK CRUD

def create_book(
    db,
    title,
    description,
    price,
    url,
    category_id
):
    book = Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category_id=category_id
    )

    db.add(book)
    db.commit()
    db.refresh(book)

    return book


def get_books(db):
    return db.query(Book).all()