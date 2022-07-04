import time

from fastapi import FastAPI, Request, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


from auth import authtentication
from db import models
from db.database import engine
from routers import blog_get
from routers import blog_post
from routers import user, article, file

# app: It's the name of the API instance. We have to use it to create endpoints
app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(authtentication.router)
app.include_router(file.router)


@app.middleware('http')
async def add_middleware(request: Request, call_next):
    """
    This middleware is now applied for all routes
    :param request:
    :param call_next:
    :return:
    """
    start_time = time.time()
    # Make any change in the request
    response = await call_next(request)
    # Make any change in the response
    duration = time.time() - start_time
    response.headers["duration"] = str(duration)
    return response

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


clients = []


@app.websocket('/chat')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    # All the clients connected to the endpoint
    clients.append(websocket)
    while True:
        data = await websocket.receive_text()
        for client in clients:
            await client.send_text(data)


# Build all models defined into models.py file
models.Base.metadata.create_all(engine)
