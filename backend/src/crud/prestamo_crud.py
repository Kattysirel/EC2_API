from sqlmodel import Session, select
from models.prestamo_model import Prestamo
from schemas.prestamo_schema import PrestamoCreate, PrestamoUpdate

def get_prestamo(session: Session, prestamo_id: int):
    return session.get(Prestamo, prestamo_id)

def get_prestamos(session: Session, skip: int = 0, limit: int = 100):
    return session.exec(select(Prestamo).offset(skip).limit(limit)).all()

def create_prestamo(session: Session, prestamo_in: PrestamoCreate):
    db_prestamo = Prestamo.model_validate(prestamo_in)
    session.add(db_prestamo)
    session.commit()
    session.refresh(db_prestamo)
    return db_prestamo

def update_prestamo(session: Session, db_prestamo: Prestamo, prestamo_in: PrestamoUpdate):
    prestamo_data = prestamo_in.model_dump(exclude_unset=True)
    db_prestamo.sqlmodel_update(prestamo_data)
    session.add(db_prestamo)
    session.commit()
    session.refresh(db_prestamo)
    return db_prestamo

def delete_prestamo(session: Session, db_prestamo: Prestamo):
    session.delete(db_prestamo)
    session.commit()
    return {"ok": True}