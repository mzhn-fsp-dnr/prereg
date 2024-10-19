from pydantic import BaseModel, UUID4

class PreregBase(BaseModel):
    pass

class CreatePrereg(PreregBase):
    department_id: str
    service_id: str

class Prereg(PreregBase):
    id: UUID4

    class Config:
        from_attributes = True