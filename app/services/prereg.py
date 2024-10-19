from sqlalchemy.orm import Session
import app.schemas.prereg_schema as prereg_schema
from app.models import prereg_model
from app.helpers import generate_random_seven_digit_number
from datetime import datetime, timedelta

def get_prereg(db_session: Session, id: str):
        return db_session.query(prereg_model.Prereg).filter(prereg_model.Prereg.id == id).first()

def get_available_slots(db_session: Session, date: datetime):
        opening_time = datetime(date.year, date.month, date.day, 8, 0)
        closing_time = datetime(date.year, date.month, date.day, 19, 0) 
        interval = timedelta(hours=1)
        
        slots = []
        current_time = opening_time
        while current_time < closing_time:
                slots.append(current_time)
                current_time += interval
                
        existing_preregs = db_session.query(prereg_model.Prereg).filter(
        prereg_model.Prereg.assigned_to >= opening_time,
        prereg_model.Prereg.assigned_to < closing_time).all()
        
        # Проверяем, какие интервалы уже заняты
        occupied_slots = {prereg.assigned_to for prereg in existing_preregs}
        
        # Создаем список свободных слотов
        available_slots = [slot for slot in slots if slot not in occupied_slots]
        return available_slots

def create_prereg(db_session: Session, prereg: prereg_schema.CreatePrereg):
        db_prereg = prereg_model.Prereg(**prereg.model_dump())
        db_prereg.code = generate_random_seven_digit_number()
        db_session.add(db_prereg)
        db_session.commit()
        db_session.refresh(db_prereg)
        return db_prereg

def delete_prereg(db_session: Session, id: str):
        db_prereg = get_prereg(db_session, id)
        if db_prereg:
                db_session.delete(db_prereg)
                db_session.commit()
        return db_prereg 