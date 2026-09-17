from fastapi import APIRouter, Depends, HTTPException, status

import src.DAL.user_repository as user_repos
from src.DAL.database import get_db

# Este controller não faz muito sentido considerando o estado atual da 
# aplicação já que não existe a funcionalidade de se inscrever em um evento.
# Contudo, um endpoint `inscricoes/{id}` é parte do exercício 3 do TP3 

router = APIRouter(prefix="/inscricoes")

@router.get("/{user_id}", status_code=status.HTTP_200_OK)
def register(user_id:int, db = Depends(get_db)):
    user = user_repos.get_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="NOT FOUND",
        )
    
    return {"id": user.id, "username": user.username, "admin": "TRUE" if user.is_admin else "FALSE"}
