from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from app.schemas.eps import EpsRead
from app.models.enums import TipoDocumento

class PacienteBase(BaseModel):
    nombre: str = Field(..., max_length=100, description="Nombre del paciente")
    apellido: str = Field(..., max_length=100, description="Apellido del paciente")
    tipo_documento: TipoDocumento = Field(..., description="Tipo de documento")
    documento: str = Field(..., max_length=20, description="Documento")
    fecha_nacimiento: Optional[datetime] = Field(default=None, description="Fecha de nacimiento")
    telefono: str = Field(..., max_length=20, description="Número de telefono")
    email: EmailStr = Field(..., max_length=100, description="Correo electrónico")
    eps_id: int = Field(..., description="ID de la eps")
    

class PacienteCreate(PacienteBase):
    pass

class PacienteUpdate(BaseModel):
    nombre: Optional[str] = Field(None, max_length=100)
    apellido: Optional[str] = Field(None, max_length=100)
    tipo_documento: Optional[TipoDocumento] = None
    documento: Optional[str] = Field(None, max_length=20)
    fecha_nacimiento: Optional[datetime] = None
    telefono: Optional[str] = Field(None, max_length=20)
    email: Optional[EmailStr] = Field(None, max_length=100)
    eps_id: Optional[int] = None

class PacienteResponse(PacienteBase):
    id: int
    eps: Optional[EpsRead] = None
    
    class Config:
        from_attributes = True

class PacienteCita(BaseModel):
    id: int
    nombre: str
    apellido: str
    documento: str
    email: str
    
    class Config:
        from_attributes = True
    