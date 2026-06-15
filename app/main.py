from app.db.db import SessionLocal

from app.db.crud import get_categories
from app.db.crud import get_books

db = SessionLocal()

print("Категории:")

for category in get_categories(db):
    print(
        f"{category.id} - {category.title}"
    )

print("\nКниги:")

for book in get_books(db):
    print(
        f"{book.id}. "
        f"{book.title} | "
        f"{book.price} руб."
    )

db.close()