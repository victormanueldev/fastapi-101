from typing import List, Dict
from fastapi import APIRouter, Depends, status, Response
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
    """
    A list of Database Models are returned, so we need to convert it manually to response
    model structure
    :param db:
    :return:
    """
    result = db_user.get_all_users(db)
    user_response = []
    for user in result:
        user_response.append(UserDisplayBase.from_orm(user))
    return user_response


@router.get('/{id_user}', status_code=status.HTTP_200_OK)
def get_user_by_id(
        id_user: int,
        db: Session = Depends(get_db)):
    """
    There was an error defining the response model so this endpoint
    has no response model for now
    :param id_user:
    :param db:
    :return:
    """
    res = db_user.get_user_by_id(db, id_user)
    user_response = UserDisplayBase.from_orm(res)
    return user_response


@router.patch('/{id_user}/update')
def update_user(
        id_user: int,
        request: UserBase,
        db: Session = Depends(get_db)):
    """
    We need to validate if there is a user with the ID provided
    :param id_user:
    :param request:
    :param db:
    :return:
    """
    result = db_user.update_user(db, id_user, request)
    return result


@router.delete('/{id_user}')
def delete_user(
        id_user: int,
        db: Session = Depends(get_db)):
    """
    We need to validate if there is a user with the ID provided
    :param id_user:
    :param db:
    :return:
    """
    return db_user.delete_user(db, id_user)
