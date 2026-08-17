from fastapi import FastAPI
from src.routers.status import router as STATUS_ROUTER
from src.routers.eventos import router as EVENTOS_ROUTER

app = FastAPI()

# ROUTERS
app.include_router(STATUS_ROUTER)
app.include_router(EVENTOS_ROUTER)
