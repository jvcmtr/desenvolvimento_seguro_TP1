from fastapi import APIRouter

router = APIRouter(prefix="/status")

@router.get("/")
def get():
    return "App ativo"