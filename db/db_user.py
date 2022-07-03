from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from db.hash import Hash


def create_user(db: Session, request: UserBase):
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


def get_all_users(db: Session):
    return db.query(DbUser).all()
