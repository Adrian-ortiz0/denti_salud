from pydantic import BaseModel
from app.models.enums import Estado
from app.schemas.eps import EpsRead
from app.models.enums import TipoDocumento

class PacienteCreate(BaseModel):
    nombre: str
    apellido: str
    tipo_documento: TipoDocumento
    documento: str
    telefono: str
    email: str
    eps_id: int

class PacienteRead(BaseModel):
    id: int
    nombre: str
    apellido: str
    tipo_documento: TipoDocumento
    documento: str
    telefono: str
    email: str
    eps_id: EpsRead
    estado: Estado
    
    class config:
        orm_mode = True