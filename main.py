from typing import Dict, Optional
from enum import Enum

from fastapi import FastAPI, status, Response
from routers import blog_get
from routers import blog_post
from routers import user, article
from db import models
from db.database import engine

# app: It's the name of the API instance. We have to use it to create endpoints
app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)


@app.get('/')
def index():
    return 'Hello World!'


# Build all models defined into models.py file
models.Base.metadata.create_all(engine)
