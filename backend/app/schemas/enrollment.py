"""Sch?mas Pydantic pour les inscriptions."""

from typing import Optional

from pydantic import BaseModel, ConfigDict

class EnrollmentBase(BaseModel):
    pass

class EnrollmentCreate(EnrollmentBase):
    pass

class EnrollmentUpdate(BaseModel):
    pass

class EnrollmentRead(EnrollmentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
