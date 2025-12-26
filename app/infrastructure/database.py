
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeBase



SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

Engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autoflush=False, bind=Engine)

class Base(DeclarativeBase):
    pass

def Get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()