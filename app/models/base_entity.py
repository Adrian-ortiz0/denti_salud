from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from .enums import *

class BaseEntity(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    estado: Estado = Field(default=Estado.ACTIVO)
    fecha_creacion: datetime = Field(default_factory=datetime.utcnow)
    fecha_modificacion: Optional[datetime] = None
    usuario_crea: Optional[str] = Field(default=None, max_length=100)
    usuario_modifica: Optional[str] = Field(default=None, max_length=100)
    
    class Config:
        # peermite actualizar fecha modificacion automaticamente
        use_enum_values = True
