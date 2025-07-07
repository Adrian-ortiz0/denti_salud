from pydantic import BaseModel
from typing import Optional
from .schemas_paciente import PacienteNombre
from .schemas_dentista import DentistaNombre

class HistoriaClinicaCreate(BaseModel):
    paciente_id: int
    dentista_id: int
    detalles_clinicos: str

class HistoriaClinicaRead(BaseModel):
    detalles_clinicos: str
    paciente: Optional[PacienteNombre]
    dentista: Optional[DentistaNombre]

    class Config:
        orm_mode = True