from sqlmodel import Session, select
from models.libro_model import Libro
from schemas.libro_schema import LibroCreate, LibroUpdate

def get_libro(session: Session, libro_id: int):
    return session.get(Libro, libro_id)

def get_libros(session: Session, skip: int = 0, limit: int = 100):
    return session.exec(select(Libro).offset(skip).limit(limit)).all()

def create_libro(session: Session, libro_in: LibroCreate):
    db_libro = Libro.model_validate(libro_in)
    session.add(db_libro)
    session.commit()
    session.refresh(db_libro)
    return db_libro

def update_libro(session: Session, db_libro: Libro, libro_in: LibroUpdate):
    libro_data = libro_in.model_dump(exclude_unset=True)
    db_libro.sqlmodel_update(libro_data)
    session.add(db_libro)
    session.commit()
    session.refresh(db_libro)
    return db_libro

def delete_libro(session: Session, db_libro: Libro):
    session.delete(db_libro)
    session.commit()
    return {"ok": True}