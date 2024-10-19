from sqlalchemy.orm import Session
import app.schemas.prereg_schema as prereg_schema
from app.models import prereg_model

def get_prereg(db_session: Session, id: str):
        return db_session.query(prereg_model.Prereg).filter(prereg_model.Prereg.id == id).first()

def create_prereg(db_session: Session, prereg: prereg_schema.CreatePrereg):
        db_prereg =  prereg_model.Prereg(**prereg.model_dump())
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