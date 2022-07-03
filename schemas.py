from pydantic import BaseModel


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

    # Converts automatically the ORM model into UserDisplayBase structure
    class Config:
        orm_mode = True
