from src.models.eventos_model import Evento

# Isso é somente um mock de um repositorio
# e funciona somente em memoria
latest_used_id = 1
eventos = [
    Evento(
        id=1,
        nome="Evento 1",
        descricao="lorem ipsum",
        organizador="joaoramos",
    ),
    Evento(
        id=2,
        nome="Evento 2",
        descricao="ESTE EVENTO NÃO PODE SER ALTERADO",
        organizador="João Cícero",
    )
]