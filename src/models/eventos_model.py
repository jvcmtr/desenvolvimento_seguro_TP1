from pydantic import BaseModel


class Evento(BaseModel):
    id: int
    nome: str
    descricao: str
    organizador: str

