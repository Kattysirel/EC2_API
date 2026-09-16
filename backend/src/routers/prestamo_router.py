from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from src.database.database import get_session
from src.crud import prestamo_crud, libro_crud
from src.schemas.prestamo_schema import PrestamoCreate, PrestamoRead, PrestamoUpdate

router = APIRouter(prefix="/prestamos", tags=["Prestamos"])

@router.post("/", response_model=PrestamoRead)
def create_prestamo(prestamo_in: PrestamoCreate, session: Session = Depends(get_session)):
    libro = libro_crud.get_libro(session=session, libro_id=prestamo_in.libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="El libro asociado no existe")
    return prestamo_crud.create_prestamo(session=session, prestamo_in=prestamo_in)

@router.get("/", response_model=list[PrestamoRead])
def read_prestamos(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    return prestamo_crud.get_prestamos(session=session, skip=skip, limit=limit)

@router.get("/{prestamo_id}", response_model=PrestamoRead)
def read_prestamo(prestamo_id: int, session: Session = Depends(get_session)):
    db_prestamo = prestamo_crud.get_prestamo(session=session, prestamo_id=prestamo_id)
    if not db_prestamo:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")
    return db_prestamo

@router.put("/{prestamo_id}", response_model=PrestamoRead)
def update_prestamo(prestamo_id: int, prestamo_in: PrestamoUpdate, session: Session = Depends(get_session)):
    db_prestamo = prestamo_crud.get_prestamo(session=session, prestamo_id=prestamo_id)
    if not db_prestamo:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")
    return prestamo_crud.update_prestamo(session=session, db_prestamo=db_prestamo, prestamo_in=prestamo_in)

@router.delete("/{prestamo_id}")
def delete_prestamo(prestamo_id: int, session: Session = Depends(get_session)):
    db_prestamo = prestamo_crud.get_prestamo(session=session, prestamo_id=prestamo_id)
    if not db_prestamo:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")
    return prestamo_crud.delete_prestamo(session=session, db_prestamo=db_prestamo)