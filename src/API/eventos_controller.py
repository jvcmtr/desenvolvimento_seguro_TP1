from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

from src.models.eventos_model import Evento
import src.DAL.eventos_repository as repos

router = APIRouter(prefix="/eventos")
templates = Jinja2Templates(directory="src/views")

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


# O ideal seria separar as views dos endpoints que trabalham puramente com respostas dados, 
@router.get("/html")
def listar_eventos_html(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="listar_eventos.html",
        context={"eventos": repos.eventos},
    )

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

