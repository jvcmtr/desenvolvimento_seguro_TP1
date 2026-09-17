from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from src.API.DTOs.User import UserCreate
from src.core.auth import verify_password, create_access_token
import src.DAL.user_repository as user_repos
from src.DAL.database import get_db

router = APIRouter(prefix="/auth")

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db = Depends(get_db)):
    user = user_repos.find_by_username(db, form_data.username)

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException( 
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Usuário ou senha incorretos"
        )

    access_token = create_access_token(data={"sub": str(user.username)})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(data: UserCreate, db = Depends(get_db)):
    user_exists = user_repos.find_by_username(db, data.username)
    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nome de usuário já cadastrado"
        )
    
    hashed_pwd = hash_password(data.password)
    new_user = user_repos.create(db, username=data.username, password_hash=hashed_pwd)
    return {"id": new_user.id, "username": new_user.username}