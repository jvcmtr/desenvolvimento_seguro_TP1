from fastapi import FastAPI
from src.API.status_controller import router as STATUS_ROUTER
from src.API.eventos_controller import router as EVENTOS_ROUTER

app = FastAPI()

# ROUTERS
app.include_router(STATUS_ROUTER)
app.include_router(EVENTOS_ROUTER)
