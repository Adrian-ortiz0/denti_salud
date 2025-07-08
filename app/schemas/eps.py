from pydantic import BaseModel, Field
from typing import Optional
from app.models.enums import Estado

class EpsBase(BaseModel):
    nombre: str = Field(..., max_length=100, description="Nombre de la EPS")

class EpsCreate(EpsBase):
    pass

class EpsUpdate(BaseModel):
    nombre: Optional[str] = Field(None, max_length=100, description="Nuevo nombre de la EPS")
    
class EpsResponse(EpsBase):
    id: int
    
    class Config:
        from_attributes = True