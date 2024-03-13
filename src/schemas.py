from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    status: bool
    created: datetime

    class Config:
        from_attributes = True


class Problem(BaseModel):
    category_id: int
    category_detail_id: int
    title: str
    content: str
    explanation: str
    subjective_answer: str | None = None

    class Config:
        from_attributes = True


class Answer(BaseModel):
    id: int
    problem_id: int
    content: str
    correct: bool

    class Config:
        from_attributes = True


class Category(BaseModel):
    id: int
    name: str
    detail: str

    class Config:
        from_attributes = True


class CategoryDetail(BaseModel):
    id: int
    name: str
    detail: str

    class Config:
        from_attributes = True