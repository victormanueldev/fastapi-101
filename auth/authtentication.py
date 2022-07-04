from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from db.database import get_db
from db.models import DbUser
from db.hash import Hash
from auth import oatuh2

router = APIRouter(
    tags=['authentication']
)


@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Open endpoint to create the access token validated with Database
    :param request: This is the OAuth form request DTO
    :param db:
    :return:
    """
    user = db.query(DbUser).filter(DbUser.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Username not found")
    if not Hash().verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")

    access_token = oatuh2.create_access_token(data={'sub': user.username})

    return {
        "access_token": access_token,
        "token_type": 'bearer'
    }
