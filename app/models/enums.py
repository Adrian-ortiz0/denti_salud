from enum import Enum

class TipoDocumento(str, Enum):
    CEDULA = "cedula"
    TARJETA_IDENTIDAD = "tarjeta_identidad"
    PASAPORTE = "pasaporte"
    
class Estado(str, Enum):
    ACTIVO = "activo"
    INACTIVO = "inactivo"
    PENDIENTE = "pendiente"