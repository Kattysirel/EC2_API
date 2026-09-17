from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database.database import get_session
from crud import libro_crud
from schemas.libro_schema import LibroCreate, LibroRead, LibroUpdate

router = APIRouter(prefix="/libros", tags=["Libros"])

@router.post("/", response_model=LibroRead)
def create_libro(libro_in: LibroCreate, session: Session = Depends(get_session)):
    return libro_crud.create_libro(session=session, libro_in=libro_in)

@router.get("/", response_model=list[LibroRead])
def read_libros(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    return libro_crud.get_libros(session=session, skip=skip, limit=limit)

@router.get("/{libro_id}", response_model=LibroRead)
def read_libro(libro_id: int, session: Session = Depends(get_session)):
    db_libro = libro_crud.get_libro(session=session, libro_id=libro_id)
    if not db_libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return db_libro

@router.put("/{libro_id}", response_model=LibroRead)
def update_libro(libro_id: int, libro_in: LibroUpdate, session: Session = Depends(get_session)):
    db_libro = libro_crud.get_libro(session=session, libro_id=libro_id)
    if not db_libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro_crud.update_libro(session=session, db_libro=db_libro, libro_in=libro_in)

@router.delete("/{libro_id}")
def delete_libro(libro_id: int, session: Session = Depends(get_session)):
    db_libro = libro_crud.get_libro(session=session, libro_id=libro_id)
    if not db_libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro_crud.delete_libro(session=session, db_libro=db_libro)