from typing import Optional
from sqlmodel import SQLModel

class PrestamoBase(SQLModel):
    nombre_usuario: str
    fecha_prestamo: str
    devuelto: bool = False
    libro_id: int

class PrestamoCreate(PrestamoBase):
    pass

class PrestamoRead(PrestamoBase):
    id: int

class PrestamoUpdate(SQLModel):
    nombre_usuario: Optional[str] = None
    fecha_prestamo: Optional[str] = None
    devuelto: Optional[bool] = None
    libro_id: Optional[int] = None