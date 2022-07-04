from typing import Dict, Optional
from enum import Enum

from fastapi import FastAPI, status, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routers import blog_get
from routers import blog_post
from routers import user, article, file
from auth import authtentication
from db import models
from db.database import engine

# app: It's the name of the API instance. We have to use it to create endpoints
app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(authtentication.router)
app.include_router(file.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# This is to make available static files in some endpoint
app.mount('/files', StaticFiles(directory='files'), name='/files')


@app.get('/')
def index():
    return 'Hello World!'


# Build all models defined into models.py file
models.Base.metadata.create_all(engine)
