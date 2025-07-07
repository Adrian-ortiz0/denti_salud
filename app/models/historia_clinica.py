from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from .base_entity import BaseEntity
from .paciente import Paciente
from .dentista import Dentista

class HistoriaClinica(BaseEntity, table=True):
    paciente_id: int = Field(foreign_key="paciente.id")
    motivo_consulta: str = Field(max_length=500)
    dentista_id: int = Field(foreign_key="dentista.id")
    diagnostico: str = Field(max_length=1000)
    observaciones: Optional[str] = Field(default=None, max_length=2000)

    paciente: Optional["Paciente"] = Relationship(back_populates="historias_clinicas")
    dentista: Optional["Dentista"] = Relationship(back_populates="historias_clinicas")