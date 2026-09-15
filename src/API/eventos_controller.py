from fastapi import APIRouter, HTTPException, Request, Depends, status
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

from src.models.eventos_model import Evento
from src.models.user_model import User

import src.DAL.eventos_repository as repos
from src.API.DTOs.Eventos import EventoCreate, EventoUpdate
from src.core.auth import get_current_user

router = APIRouter(prefix="/eventos")
templates = Jinja2Templates(directory="src/views")

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

@router.put("/{id}", response_model=Evento)
def update_evento(
    evento_id: int,
    updated_evento: EventoUpdate,
    current_user: User = Depends(get_current_user)
):
    evento = None
    try:
        # É preciso urgentemente melhorar o repositorio
        evento = [e for e in repos.eventos if e.id == evento_id][0]
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Evento não encontrado"
        )

    if evento.organizador != current_user.username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado"
        )

    if dados_atualizacao.nome is not None:
        evento.nome = dados_atualizacao.nome
    if dados_atualizacao.descricao is not None:
        evento.descricao = dados_atualizacao.descricao

    return evento

