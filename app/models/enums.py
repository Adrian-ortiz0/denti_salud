from enum import Enum

class TipoDocumento(str, Enum):
    CEDULA = "cedula"
    TARJETA_IDENTIDAD = "tarjeta_identidad"
    PASAPORTE = "pasaporte"
    
class Estado(str, Enum):
    ACTIVO = "activo"
    INACTIVO = "inactivo"
    PENDIENTE = "pendiente"
    
class EstadoCita(str, Enum):
    PROGRAMADA = "programada"
    CONFIRMADA = "confirmada"
    EN_CURSO = "en_curso"
    COMPLETADA = "completada"
    CANCELADA = "cancelada"
    NO_ASISTIO = "no_asistio"