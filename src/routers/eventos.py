from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/eventos")

# Model
class Evento(BaseModel):
    id: int
    nome: str
    descricao: str
    organizador: str

# DTO create
class EventoCreate(BaseModel):
    nome: str
    descricao: str
    organizador: str


# Repositorio local em memoria
latest_used_id = 1
eventos = [
    Evento(
        id=1,
        nome="Evento 1",
        descricao="lorem ipsum",
        organizador="João Cícero",
    )
]

@router.post("/", response_model=Evento)
def create_evento(ev: EventoCreate):
    latest_used_id += 1
    evento = Evento(
        id=latest_used_id,
        name=ev.name,
        descricao=ev.descricao,
        organizador=ev.organizador
    )

    eventos.append(evento)
    return evento

@router.get("/", response_model=list[Evento])
def get_all_eventos():
    return eventos

@router.get("/{id}", response_model=Evento)
def get_evento(id: int):
    for evento in eventos:
        if evento.id == id:
            return evento

    raise HTTPException(
        status_code=404,
        detail="NOT FOUND",
    )


