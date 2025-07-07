from .base_entity import BaseEntity
from sqlmodel import Field
from datetime import datetime

class Cita(BaseEntity, table=True):
    paciente_id: int = Field(foreign_key="paciente.id")
    dentista_id: int = Field(foreign_key="dentista.id")
    fecha_hora: datetime