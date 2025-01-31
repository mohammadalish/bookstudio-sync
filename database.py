from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_FULL_URL = os.getenv("DATABASE_FULL_URL")

engine = create_engine(DATABASE_FULL_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


print("DATABASE_FULL_URL:", os.getenv("DATABASE_FULL_URL"))
