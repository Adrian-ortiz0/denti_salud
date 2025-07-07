from sqlmodel import Field, Relationship
from typing import Optional
from datetime import datetime
from .base_entity import BaseEntity
from .enums import EstadoCita

class Cita(BaseEntity, table=True):
    __tablename__ = "cita"
    
    motivo: str = Field(max_length=500)
    estado_cita: EstadoCita = Field(default=EstadoCita.PROGRAMADA)
    paciente_id: int = Field(foreign_key="paciente.id")
    dentista_id: int = Field(foreign_key="dentista.id")
    fecha_hora: datetime
    
    paciente: Optional["Paciente"] = Relationship(back_populates="citas")
    dentista: Optional["Dentista"] = Relationship(back_populates="citas")