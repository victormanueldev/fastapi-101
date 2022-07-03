from typing import List
from pydantic import BaseModel


class Article(BaseModel):
    """
    Class inside UserDisplayBase
    """
    title: str
    content: str
    published: bool

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    """
    DTO Request
    """
    username: str
    email: str
    password: str


class UserDisplayBase(BaseModel):
    """
    DTO Response
    """
    username: str
    email: str
    items: List[Article] = []

    # Converts automatically the ORM model into UserDisplayBase structure
    class Config:
        orm_mode = True


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


class ArticleDisplayBase(BaseModel):
    title: str
    content: str
    published: bool
    user: User

    class Config:
        orm_mode = True