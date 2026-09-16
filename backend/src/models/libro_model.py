from typing import Optional
from sqlmodel import Field, SQLModel

class Libro(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str = Field(index=True)
    autor: str
    isbn: str = Field(unique=True)
    stock: int = Field(default=1)