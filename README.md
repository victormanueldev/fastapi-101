<p>
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>
<p>
    FastAPI framework, high performance, easy to learn, fast to code, ready for production</em>
</p>

---

In this project FastAPI was implemented and the following topics were applied in code:

- RestAPIs with FastAPI features
- Auto documented API with Swagger and ReDoc
- Path and query parameters
- HTTP status, codes and exceptions
- Error handling
- Tags
- Routers and automatic path generation
- API responses and response management
- Validators
- Complex subtypes
- SQL, relational database management and ORM
- SQLAlchemy
- Authentication and authorization
- File management
- API deployment
- Testing and debugging
- Middleware
- Async programming
- Web socket communication 
- Background tasks 
- Dependency Injection

## Installation
```bash
$ pip3 install -r requirements.txt
```

## Running the app
```bash
#Development
$ uvicorn main:app

# Watch mode
$ uvicorn main:app --reload
```

## Tests
```bash
$ pytest -v
```