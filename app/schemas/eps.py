from pydantic import BaseModel
from app.models.enums import Estado

class EpsCreate(BaseModel):
    nombre: str

class EpsRead(BaseModel):
    id: int
    nombre: str
    estado: Estado
    
    class Config:
        orm_mode = True