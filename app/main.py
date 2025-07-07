from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv
from sqlalchemy.exc import OperationalError
import time
import os

# importar los modelos para que SQLModel cree las tablas

from app.models import *

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

app = FastAPI()

def connect_with_retry(retries=5, delay=3):
    for attempt in range(retries):
        try:
            with engine.connect() as conn:
                return True
        except OperationalError:
            print(f"DB no lista, reintentando en {delay} segundos... (Intento {attempt+1}/{retries})")
            time.sleep(delay)
    raise RuntimeError("No se pudo conectar a la base de datos tras varios intentos.")


@app.on_event("startup")
def on_startup():
    connect_with_retry(retries=10, delay=3) 
    SQLModel.metadata.create_all(engine)

@app.get("/")
def read_root():
    return {"mensaje": "clinica odontologica"}