from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from db.database import get_db
from schemas import UserBase, UserDisplayBase
from db import db_user


router = APIRouter(prefix='/user', tags=['user'])


# Create
@router.post('/', response_model=UserDisplayBase)
def create_user(user: UserBase, db: Session = Depends(get_db)):
    """
    Creates a new user into databse and return the result
    :param user:
    :param db:
    :return: [Dict] {username, email}
    """
    res = db_user.create_user(db, user)
    # Ref: https://pydantic-docs.helpmanual.io/usage/models/#orm-mode-aka-arbitrary-class-instances
    user_response = UserDisplayBase.from_orm(res)
    return user_response


# Read
@router.get('/', response_model=List[UserDisplayBase])
def get_all_users(db: Session = Depends(get_db)):
    result = db_user.get_all_users(db)
    user_response = []
    for user in result:
        user_response.append(UserDisplayBase.from_orm(user))
    return user_response
# Update

# Delete
