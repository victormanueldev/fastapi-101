from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from auth.oatuh2 import get_current_user
from db import db_article
from db.database import get_db
from schemas import ArticleBase, ArticleDisplayBase, UserDisplayBase

router = APIRouter(prefix='/article', tags=['article'])


@router.post('/', response_model=ArticleDisplayBase)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    res = db_article.create_article(db, request)
    user_response = ArticleDisplayBase.from_orm(res)
    return user_response


@router.get('/{id_article}')
def get_article_by_id(
        id_article: int,
        db: Session = Depends(get_db),
        current_user: UserDisplayBase = Depends(get_current_user)):
    """
    We can get the user in every endpoint by using Dependency Injection
    :param id_article:
    :param db:
    :param current_user:
    :return:
    """
    res = db_article.get_article_by_id(db, id_article)
    user_response = ArticleDisplayBase.from_orm(res)
    return {
        'data': user_response,
        'current_user': current_user
    }
