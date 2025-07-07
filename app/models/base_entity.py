from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from .enums import *

class BaseEntity(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    estado: Estado = Field(default=Estado.ACTIVO)
    fecha_creacion: datetime = Field(default=datetime.utcnow)
    fecha_modificacion: Optional[datetime] = None
    usuario_crea: Optional[str] = None
    usuario_modifica: Optional[str] = None