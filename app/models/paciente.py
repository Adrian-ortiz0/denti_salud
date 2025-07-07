from .base_entity import BaseEntity
from sqlmodel import Field

class Paciente(BaseEntity, table=True):
    nombre: str
    apellido: str
    tipo_documento: str
    documento: str
    telefono: str
    eps_id: int = Field(foreign_key="eps.id")