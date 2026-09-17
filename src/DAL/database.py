import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")
os.makedirs(DATA_DIR, exist_ok=True)

DB_PATH = os.path.join(DATA_DIR, "eventos_api.db")

engine = create_engine( f"sqlite:///{DB_PATH}", connect_args={"check_same_thread": False})

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()