

```
pip install fastapi[standard] uvicorn sqlalchemy pydantic
```


```
app/
├── domain/          # INNERMOST: Entities and Repository Interfaces (No external deps)
├── application/     # INNER: Use Cases / Services (Depends only on Domain)
├── infrastructure/  # OUTER: Database implementation (SQLAlchemy, SQLite)
├── api/             # OUTERMOST: FastAPI Routers and DTOs
└── main.py          # Entry point
```