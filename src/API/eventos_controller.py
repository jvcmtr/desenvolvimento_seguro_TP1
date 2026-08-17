from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.models.eventos_model import Evento
import src.DAL.eventos_repository as repos

router = APIRouter(prefix="/eventos")

# Mesmo com a separação em camadas, ainda é interessante manter os DTOs exclusivos da camada de 
# aplicação e definição dos endpoints separados dos demais modelos 
 
# DTO create
class EventoCreate(BaseModel):
    nome: str
    descricao: str
    organizador: str


# Endpoints
@router.post("/", response_model=Evento)
def create_evento(ev: EventoCreate):
    repos.latest_used_id += 1
    evento = Evento(
        id=repos.latest_used_id ,
        nome=ev.nome,
        descricao=ev.descricao,
        organizador=ev.organizador
    )

    repos.eventos.append(evento)
    return evento

@router.get("/", response_model=list[Evento])
def get_all_eventos():
    return repos.eventos

@router.get("/{id}", response_model=Evento)
def get_evento(id: int):
    for evento in repos.eventos:
        if evento.id == id:
            return evento

    raise HTTPException(
        status_code=404,
        detail="NOT FOUND",
    )

