from typing import List
from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from db.hash import Hash


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
    return db.query(DbUser).filter(DbUser.id == id_user).first()


def update_user(db: Session, id_user: int, request: UserBase):
    """
    Repository to partial update to user filtered by ID
    :param db:
    :param id_user:
    :param request:
    :return:
    """
    user = db.query(DbUser).filter(DbUser.id == id_user)
    if user is not None:
        user.update({
            DbUser.username: request.username,
            DbUser.email: request.email,
            DbUser.password: Hash().bcrypt(request.password)
        })
        db.commit()
        return 'OK'
    else:
        return None


def delete_user(db: Session, id_user: int):
    """
    Repository to delete a user filtered by ID
    :param db:
    :param id_user:
    :return:
    """
    user = db.query(DbUser).filter(DbUser.id == id_user).first()
    if user is not None:
        db.delete(user)
        db.commit()
        return 'OK'
    else:
        return None
