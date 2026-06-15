from pydantic import BaseModel


# CATEGORY


class CategoryBase(BaseModel):
    title: str


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True


# BOOK


class BookBase(BaseModel):
    title: str
    description: str
    price: float
    url: str
    category_id: int


class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True