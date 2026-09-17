from typing import List, Optional
from sqlalchemy.orm import Session

from src.DAL.db_models.eventos_table import EventoTable
from src.API.DTOs.Eventos import EventoCreate, EventoUpdate

def get_all(db: Session) -> List[EventoTable]:
    return db.query(EventoTable).all()

def get_by_id(db: Session, evento_id: int) -> Optional[EventoTable]:
    return db.query(EventoTable).filter(EventoTable.id == evento_id).first()

def create(db: Session, ev: EventoCreate) -> EventoTable:
    novo_evento = EventoTable(
        nome=ev.nome,
        descricao=ev.descricao,
        organizador=ev.organizador
    )
    db.add(novo_evento)
    db.commit()
    db.refresh(novo_evento)
    return novo_evento

def update(db: Session, evento_id: int, updated_evento: EventoUpdate) -> Optional[EventoTable]:
    evento = get_by_id(db, evento_id)
    if not evento:
        return None

    if updated_evento.nome is not None:
        evento.nome = updated_evento.nome
    if updated_evento.descricao is not None:
        evento.descricao = updated_evento.descricao

    db.commit()
    db.refresh(evento)
    return evento

def search_by_name(db: Session, nome: str):
    # Permitindo SQL Injection afim de cumprir com a questão 1
    query_raw = f"SELECT id, nome, descricao, organizador FROM eventos WHERE nome LIKE '%{nome}%'"
    result = db.execute(text(query_raw))
    return result.mappings().all()