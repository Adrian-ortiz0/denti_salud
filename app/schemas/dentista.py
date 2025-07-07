from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from app.models.enums import Estado

class DentistaCreate(BaseModel):
    nombre: str
    apellido: str
    tipo_documento: str
    documento: str
    telefono: str
    especialidad: str

class DentistaRead(BaseModel):
    nombre: str
    apellido: str
    tipo_documento: str
    documento: str
    telefono: str
    especialidad: str