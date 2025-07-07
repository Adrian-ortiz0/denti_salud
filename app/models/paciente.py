from .base_entity import BaseEntity
from sqlmodel import Field, Relationship
from sqlalchemy import Column, Enum as SQLEnum
from .enums import TipoDocumento
from datetime import datetime
from typing import Optional, List

class Paciente(BaseEntity, table=True):
    __tablename__ = "paciente"
    
    nombre: str = Field(max_length=100)
    apellido: str = Field(max_length=100)
    tipo_documento: TipoDocumento=Field(sa_column = Column(SQLEnum(TipoDocumento)))
    documento: str = Field(max_length=20, unique=True, index=True)
    fecha_nacimiento: Optional[datetime] = Field(default=None)
    telefono: str = Field(max_length=20)
    email: str = Field(max_length=100, unique=True, index=True)
    
    # foreign key
    eps_id: int = Field(foreign_key="eps.id")
    
    # relaciones
    eps: Optional["Eps"] = Relationship(back_populates="pacientes")
    citas: List["Cita"] = Relationship(back_populates="paciente")
    historias_clinicas: List["HistoriaClinica"] = Relationship(back_populates="paciente")
