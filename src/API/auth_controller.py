from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from src.core.auth import verify_password, create_access_token
import src.DAL.user_repository as user_repos

router = APIRouter(prefix="/auth")

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_repos.find_by_username(form_data.username)

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException( 
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Usuário ou senha incorretos"
        )

    access_token = create_access_token(data={"sub": str(user.username)})
    return {"access_token": access_token, "token_type": "bearer"}