from pydantic import BaseModel
# Mesmo com a separação em camadas, ainda é interessante manter os DTOs exclusivos da camada de
# API separados dos demais modelos. 
 
# DTO create
class EventoCreate(BaseModel):
    nome: str
    descricao: str

class EventoUpdate(BaseModel):
    nome: str | None = None
    descricao: str | None = None