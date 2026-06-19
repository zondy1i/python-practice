from app.db.models import Category
from app.db.models import Book


def create_category(db, title):
    category = Category(title=title)

    db.add(category)
    db.commit()
    db.refresh(category)

    return category


def get_categories(db):
    return db.query(Category).all()


def get_category(db, category_id):
    return db.query(Category).filter(
        Category.id == category_id
    ).first()


def update_category(
    db,
    category_id,
    new_title
):
    category = get_category(
        db,
        category_id
    )

    if category:
        category.title = new_title
        db.commit()
        db.refresh(category)

    return category


def delete_category(
    db,
    category_id
):
    category = get_category(
        db,
        category_id
    )

    if category:
        db.delete(category)
        db.commit()

    return category


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


def get_book(
    db,
    book_id
):
    return db.query(Book).filter(
        Book.id == book_id
    ).first()


def update_book(
    db,
    book_id,
    data
):
    book = get_book(
        db,
        book_id
    )

    if book:
        book.title = data.title
        book.description = data.description
        book.price = data.price
        book.url = data.url
        book.category_id = data.category_id

        db.commit()
        db.refresh(book)

    return book


def delete_book(
    db,
    book_id
):
    book = get_book(
        db,
        book_id
    )

    if book:
        db.delete(book)
        db.commit()

    return book