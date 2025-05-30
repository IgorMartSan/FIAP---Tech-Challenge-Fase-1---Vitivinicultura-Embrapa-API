from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from core.settings import settings
from sqlalchemy.exc import OperationalError


Base = declarative_base()

DATABASE_URL = (
    f"{settings.DB_DRIVERNAME}://{settings.DB_USER}:{settings.DB_PASSWORD}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_DATABASENAME}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



