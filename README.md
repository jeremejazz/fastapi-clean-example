# Fast API Clean Architecture Example

Simple clean architecture example implementation in FastAPI.

## Setup

Assuming you are working on a virtual environment like [venv](https://docs.python.org/3/library/venv.html), install the dependencies:

```
pip install -r requirements.txt
```

## Directory Structure

```
app/
├── domain/          # INNERMOST: Entities and Repository Interfaces (No external deps)
├── application/     # INNER: Use Cases / Services (Depends only on Domain)
├── infrastructure/  # OUTER: Database implementation (SQLAlchemy, SQLite)
├── api/             # OUTERMOST: FastAPI Routers and DTOs
└── main.py          # Entry point
```