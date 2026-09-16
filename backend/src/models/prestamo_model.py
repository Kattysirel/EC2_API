from typing import Optional
from sqlmodel import Field, SQLModel

class Prestamo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre_usuario: str
    fecha_prestamo: str
    devuelto: bool = Field(default=False)
    libro_id: int = Field(foreign_key="libro.id")