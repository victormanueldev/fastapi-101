from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from db.hash import Hash
from db.models import DbUser
from schemas import UserBase


def create_user(db: Session, request: UserBase) -> DbUser:
    """
    Repository handles all CRUD operations using the ORM Model
    :param db:
    :param request:
    :return:
    """
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash().bcrypt(request.password)
    )
    # Creates new user
    db.add(new_user)
    # Send command to the database
    db.commit()
    # To retrieve the ID created by DB
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session) -> List[DbUser]:
    """
    Repository to read all elements of a table from the database
    :param db:
    :return:
    """
    return db.query(DbUser).all()


def get_user_by_id(db: Session, id_user: int) -> DbUser:
    """
    Repository to get an user filtered by ID
    :param db:
    :param id_user:
    :return:
    """
    user = db.query(DbUser).filter(DbUser.id == id_user).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with {id_user} not found')
    return user


def get_user_by_username(db: Session, username: str) -> DbUser:
    """
    Repository to get an user filtered by Username
    :param db:
    :param username:
    :return:
    """
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with {username} not found')
    return user


def update_user(db: Session, id_user: int, request: UserBase):
    """
    Repository to partial update to user filtered by ID
    :param db:
    :param id_user:
    :param request:
    :return:
    """
    user = db.query(DbUser).filter(DbUser.id == id_user)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with {id_user} not found')
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash().bcrypt(request.password)
    })
    db.commit()
    return 'OK'


def delete_user(db: Session, id_user: int):
    """
    Repository to delete a user filtered by ID
    :param db:
    :param id_user:
    :return:
    """
    user = db.query(DbUser).filter(DbUser.id == id_user).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with {id_user} not found')
    db.delete(user)
    db.commit()
    return 'OK'
