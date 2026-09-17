from pydantic import BaseModel


class Evento(BaseModel):
    id: int | None
    nome: str
    descricao: str
    organizador: str

