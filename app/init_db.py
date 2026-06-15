from app.db.db import Base
from app.db.db import engine
from app.db.db import SessionLocal

from app.db.crud import create_category
from app.db.crud import create_book


Base.metadata.create_all(bind=engine)

db = SessionLocal()

fiction = create_category(
    db,
    "Художественная литература"
)

programming = create_category(
    db,
    "Программирование"
)

create_book(
    db,
    "1984",
    "Антиутопия",
    500,
    "",
    fiction.id
)

create_book(
    db,
    "Мастер и Маргарита",
    "Роман Булгакова",
    650,
    "",
    fiction.id
)

create_book(
    db,
    "Изучаем Python",
    "Для начинающих",
    1200,
    "",
    programming.id
)

create_book(
    db,
    "Fluent Python",
    "Продвинутый уровень",
    1800,
    "",
    programming.id
)

db.close()

print("Данные добавлены")