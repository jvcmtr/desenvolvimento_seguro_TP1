from fastapi import APIRouter, HTTPException, Request, Depends, status
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

from src.models.eventos_model import Evento
from src.models.user_model import User

import src.DAL.eventos_repository as repos
from src.DAL.database import get_db

from src.API.DTOs.Eventos import EventoCreate, EventoUpdate
from src.core.auth import get_current_user

router = APIRouter(prefix="/eventos")
templates = Jinja2Templates(directory="src/views")

# Endpoints
@router.post("/", response_model=Evento)
def create_evento(ev: EventoCreate, current_user = Depends(get_current_user), db = Depends(get_db)):
    
    ev = Evento(
        id = None,
        nome = ev.nome,
        descricao = ev.descricao,
        organizador = current_user.username
    )

    return repos.create(db, ev)

@router.get("/busca")
def buscar_evento_por_nome(nome: str, db = Depends(get_db)):
    QUERY_WHITELIST = r"abcdefghijklmnopqrstuvwxyz0123456789-=+[]{}:;.,/"
    
    for c in nome:
        if c not in QUERY_WHITELIST:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Caractere inválido encontrado no input: {c}"
            )
    
    return repos.search_by_name(db, nome)

# O ideal seria separar as views dos endpoints que trabalham puramente com respostas dados, 
@router.get("/html")
def listar_eventos_html(request: Request, db = Depends(get_db)):
    return templates.TemplateResponse(
        request=request,
        name="listar_eventos.html",
        context={"eventos": repos.get_all(db)},
    )

@router.get("/", response_model=list[Evento])
def get_all_eventos( db = Depends(get_db)):
    return repos.get_all(db)

@router.get("/{id}", response_model=Evento)
def get_evento(id: int, db = Depends(get_db)):
    ev = repos.get_by_id(db, id)
    if ev: return ev

    raise HTTPException(
        status_code=404,
        detail="NOT FOUND",
    )

@router.put("/{id}", response_model=Evento)
def update_evento(
    id: int,
    updated_evento: EventoUpdate,
    current_user: User = Depends(get_current_user),
    db = Depends(get_db) ):

    ev = repos.get_by_id(db, id)
    if not ev:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Evento não encontrado"
        )
    
    if evento.organizador != current_user.username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado"
        )
    repos.update(db, id, updated_evento)
