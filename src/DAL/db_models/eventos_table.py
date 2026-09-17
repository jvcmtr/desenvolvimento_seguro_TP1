from sqlalchemy import Column, Integer, String, Boolean
from src.DAL.database import Base

class EventoTable(Base):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    organizador = Column(String, nullable=False)