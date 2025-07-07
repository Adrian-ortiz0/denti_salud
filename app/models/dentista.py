from .base_entity import BaseEntity

class Dentista(BaseEntity, table=True):
    nombre: str
    apellido: str
    tipo_documento: str
    documento: str
    telefono: str
    especialidad: str