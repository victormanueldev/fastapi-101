from typing import List, Dict
from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm.session import Session

from db.database import get_db
from schemas import ArticleBase, ArticleDisplayBase
from db import db_article


router = APIRouter(prefix='/article', tags=['article'])


@router.post('/', response_model=ArticleDisplayBase)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    res = db_article.create_article(db, request)
    user_response = ArticleDisplayBase.from_orm(res)
    return user_response


@router.get('/{id_article}', response_model=ArticleDisplayBase)
def get_article_by_id(
        id_article: int,
        db: Session = Depends(get_db),
        response: Response = Response(status_code=status.HTTP_200_OK)):
    res = db_article.get_article_by_id(db, id_article)
    if res is not None:
        user_response = ArticleDisplayBase.from_orm(res)
        return user_response
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'User with id {id_article} was not found'}