from contextlib import asynccontextmanager
from fastapi import FastAPI
from database.database import create_database
from routers import libro_router, prestamo_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_database()
    yield

app = FastAPI(
    title="API Biblioteca Digital",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(libro_router.router)
app.include_router(prestamo_router.router)

@app.get("/")
def root():
    return {"message": "API de Biblioteca Digital funcionando correctamente"}