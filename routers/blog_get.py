from typing import Dict, Optional, List
from enum import Enum

from fastapi import APIRouter, Header, Cookie
from fastapi import status, Response

router = APIRouter(prefix='/blog', tags=['blog'])


@router.get(
    '/all',
    summary='Retrieve all blogs',
    description='This API call simulates fetching all blogs',
    response_description='Retrieve all existing blogs'
)
def get_blogs(response: Response, custom_header: Optional[List[str]] = Header(None)):
    """
    The order is important because there is a match between /all and parameter
    /{id_blog}.
    Handling response and request headers
    Handling cookies
    :return:
    """
    response.headers['custom-response-header'] = ', '.join(custom_header)
    response.set_cookie(key='test_cookie', value='Some test string cookie value')
    return custom_header


@router.get('/all-page')
def get_paginated_blogs(page=1, page_size: Optional[int] = None, test_cookie: Optional[str] = Cookie(None)) -> Dict:
    """
    Every parameter of the function that is not present in the URL,
    is considered as Query Parameter. Data type validations are made for query params.
    If there is any cookie stored into the client this will be sent in the request
    :param page:
    :param page_size:
    :param test_cookie:
    :return:
    """
    return {'message': f'All {page_size} blogs on page {page}', 'cookie': f'{test_cookie}'}


@router.get('/{id}/comments/{comment_id}')
def get_blog_comments(id: str, comment_id: str, valid: bool = True, username: Optional[str] = None):
    return {'message': f'Blog ID {id}, comment ID {comment_id}, valid: {valid}, username: {username}'}


@router.get('/{id_blog}', status_code=status.HTTP_200_OK)
def get_blog_by_id(id_blog: int, response: Response) -> Dict:
    """
    We have to define the type parameter that we will pass in the endpoint
    :param id_blog:
    :param response:
    :return: A message with ID
    """
    if id_blog > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog with id {id_blog} was not found'}
    response.status_code = status.HTTP_200_OK
    return {'message': f'Blog with id: {id_blog}'}


class BlogType(str, Enum):
    """
    This class validates the type of the parameter sent in the request
    """
    short = 'short'
    story = 'story'
    howto = 'howto'


@router.get('/type/{type}')
def get_blog_by_type(type: BlogType) -> Dict:
    """
    If we don't define the data type of param, we will get
    an HTTP 422 error Unprocessable entity
    :param type: BlogType
    :return: Dict with type
    """
    return {'message': f'Blog with type {type}'}
