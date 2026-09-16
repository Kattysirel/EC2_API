from typing import Optional
from sqlmodel import SQLModel

class LibroBase(SQLModel):
    titulo: str
    autor: str
    isbn: str
    stock: int = 1

class LibroCreate(LibroBase):
    pass

class LibroRead(LibroBase):
    id: int

class LibroUpdate(SQLModel):
    titulo: Optional[str] = None
    autor: Optional[str] = None
    isbn: Optional[str] = None
    stock: Optional[int] = None