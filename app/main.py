from fastapi import FastAPI

from app.api.categories import router as category_router
from app.api.books import router as book_router

app = FastAPI()

app.include_router(category_router)
app.include_router(book_router)


@app.get("/health")
def health():
    return {
        "status": "ok"
    }