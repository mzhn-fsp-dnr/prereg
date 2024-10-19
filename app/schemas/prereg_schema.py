from pydantic import BaseModel, UUID4
from datetime import datetime

class PreregBase(BaseModel):
    pass

class CreatePrereg(PreregBase):
    department_id: str
    service_id: str
    assigned_to: datetime

class GetAvailablePreregDate(PreregBase):
    date: datetime

class Prereg(PreregBase):
    id: UUID4
    assigned_to: datetime

    class Config:
        from_attributes = True