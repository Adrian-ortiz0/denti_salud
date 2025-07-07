from sqlmodel import Field, Relationship
from typing import Optional, List
from sqlalchemy import Column, Enum as SQLEnum
from .base_entity import BaseEntity
from .enums import TipoDocumento

class Dentista(BaseEntity, table=True):
    nombre: str = Field(max_length=100)
    apellido: str = Field(max_length=100)
    tipo_documento: TipoDocumento=Field(sa_column = Column(SQLEnum(TipoDocumento)))
    documento: str = Field(max_length=20, unique=True, index=True)
    telefono: str = Field(max_length=20)
    especialidad: str = Field(max_length=100)
    
    citas: List["Cita"] = Relationship(back_populates="dentista")
    historias_clinicas: List["HistoriaClinica"] = Relationship(back_populates="dentista")