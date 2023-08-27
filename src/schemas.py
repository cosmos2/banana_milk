from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    status: bool
    created: str

    class Config:
        orm_mode = True


class Problem(BaseModel):
    id: int
    category_id: int
    category_detail_id: int
    title: str
    content: str

    class Config:
        orm_mode = True


class Category(BaseModel):
    id: int
    name: str
    detail: str

    class Config:
        orm_mode = True


class CategoryDetail(BaseModel):
    id: int
    name: str
    detail: str

    class Config:
        orm_mode = True