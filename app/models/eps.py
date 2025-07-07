from .base_entity import BaseEntity
from sqlmodel import Field, Relationship
from typing import Optional, List

class Eps(BaseEntity, table=True):
    __tablename__ = "eps"
    
    nombre: str
    usuarios: List[str] = Relationship(back_populates="eps")