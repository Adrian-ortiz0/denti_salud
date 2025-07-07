from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PacienteNombre(BaseModel):
    nombre: str
    apellido: str

    class Config:
        orm_mode = True


class DentistaNombre(BaseModel):
    nombre: str
    apellido: str

    class Config:
        orm_mode = True


class CitaCreate(BaseModel):
    paciente_id: int
    dentista_id: int
    fecha_hora: datetime


class CitaRead(BaseModel):
    fecha_hora: datetime
    paciente: Optional[PacienteNombre]
    dentista: Optional[DentistaNombre]

    class Config:
        orm_mode = True