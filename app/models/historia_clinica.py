from .base_entity import BaseEntity
from sqlmodel import Field

class HistoriaClinica(BaseEntity, table=True):
    paciente_id: int = Field(foreign_key="paciente.id")
    dentista_id: int = Field(foreign_key="dentista.id")
    detalles_clinicos: str