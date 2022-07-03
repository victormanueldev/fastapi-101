from db.models import DbArticle
from schemas import ArticleBase
from sqlalchemy.orm.session import Session


def create_article(db: Session, request: ArticleBase):
    new_article = DbArticle(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.creator_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_article_by_id(db: Session, id_article: int):
    article = db.query(DbArticle).filter(DbArticle.id == id_article).first()
    return article
