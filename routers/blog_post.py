from typing import Dict, Optional, List
from enum import Enum

from fastapi import APIRouter
from fastapi import status, Response, Body, Path, Query, Depends
from pydantic import BaseModel

router = APIRouter(prefix='/blog', tags=['blog'])


class ImageModel(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    """
    This class defines the DTO for an entity so that we can see this
    schema in the swagger. Validates the properties and its types.
    Converts json to a Python object
    """
    title: str
    content: str
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] ={}
    image: Optional[ImageModel] = None


@router.post('/')
def create_blog(blog: BlogModel):
    """
    This parameter convert the body to an object of BlogModel class
    :param blog:
    :return:
    """
    return blog


@router.post('/{id_post}/comment')
def create_comment_post(
        blog: BlogModel,
        id_post: int = Path(None, description='Blog ID'),
        comment_id: int = Query(None, description='Comment ID', deprecated=True),
        comment: str = Body(..., min_length=10, max_length=51, regex=r'.*')):
    """
    We can specify the default value of each parameter to give more context to the function.
    Each class Query, Path, Body has metadata like title, desc, etc...
    ... is to make a body parameter required
    Body, Path and Query classes have built-in validators for strings and numbers
    :param blog:
    :param id_post:
    :param comment_id:
    :param comment:
    :return:
    """
    return {"id": id_post, "data": blog, "comment_id": comment_id, "comment": comment}


@router.post('/{id_post}/versions')
def create_blog_with_versions(blog: BlogModel, id_post: int, v: Optional[List[str]] = Query(None)):
    """
    We can define a query parameter to be a list in order to receive a bunch of
    query parameters with same name
    :param blog:
    :param id_post:
    :param v:
    :return:
    """
    return {"id": id_post, "data": blog, "version": v}


@router.post('/{id_post}')
def create_blog_by_id(blog: BlogModel, id_post: int, version: int = 1):
    """
    If there is a parameter that inherit from base model, FastAPI will understand it
    as a request body, all remaining will be treated as query or path parameters.
    :param blog:
    :param id_post:
    :param version:
    :return:
    """
    return {"id": id_post, "data": blog, "version": version}



