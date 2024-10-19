from sqlalchemy import Column, DateTime, UUID, Integer
from app.models.base import Base
import uuid
import datetime

class Prereg(Base):
    __tablename__ = "preregs"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code = Column(Integer, nullable=False)
    department_id = Column(UUID(as_uuid=True), nullable=False)
    service_id = Column(UUID(as_uuid=True), nullable=False)
    
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow) 