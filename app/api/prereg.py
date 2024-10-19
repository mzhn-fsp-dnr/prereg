from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas import prereg_schema
import app.services.prereg as prereg_service
from uuid import UUID
from datetime import datetime

router = APIRouter(prefix="/prereg")

@router.get("/validate/{code}")
def validate_code(code: int, db_session: Session = Depends(get_db)):
    return prereg_service.validate_code(db_session, code)

@router.get("/slots/{date}")
def get_available(date: datetime, db_session: Session = Depends(get_db)):
    return prereg_service.get_available_slots(db_session, date)

@router.get("/office/{office_id}/{code}")
def get_prereg_by_office_id_and_code(office_id: str, code: int, db_session: Session = Depends(get_db)):
    return prereg_service.get_prereg_by_office_id_and_code(db_session, office_id, code)

@router.post("/")
def create_prereg(prereg: prereg_schema.CreatePrereg, db_session: Session = Depends(get_db)):
    """
    Получение талона на пререгу
    """
    return prereg_service.create_prereg(db_session, prereg)

@router.delete("/{id}")
def delete_prereg(id: UUID, db_session: Session = Depends(get_db)):
    """"Удаление талона пререги"""
    
    found = prereg_service.delete_prereg(db_session, id)
    if not found:
        raise HTTPException(status_code=404, detail="Талон предварительной записи не найден")
    return found

@router.get("/{id}")
def get_prereg(id: UUID, db_session: Session = Depends(get_db)):
    """Получение пререги по id"""
    
    found = prereg_service.get_prereg(db_session, id) 
    if not found:
        raise HTTPException(status_code=404, detail="Талон предварительной записи не найден")
    
    return found