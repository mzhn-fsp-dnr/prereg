from pydantic import BaseModel, UUID4
from typing import Optional, List

class PreregBase(BaseModel):
    pass

class CreatePrereg(PreregBase):
    code: int
    department_id: str
    service_id: str

class Prereg(PreregBase):
    id: UUID4

    class Config:
        from_attributes = True