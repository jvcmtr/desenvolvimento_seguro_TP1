# Mesmo com a separação em camadas, ainda é interessante manter os DTOs exclusivos da camada de
# API separados dos demais modelos. 
 
# DTO create
class EventoCreate(BaseModel):
    nome: str
    descricao: str
    organizador: str