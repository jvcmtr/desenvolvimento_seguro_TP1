from sqlalchemy import Column, Integer, String, Boolean
from src.DAL.database import Base

class UserTable(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)