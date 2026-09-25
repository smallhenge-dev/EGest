"""Sch?mas Pydantic pour les mati?res."""

from typing import Optional

from pydantic import BaseModel, ConfigDict

class SubjectBase(BaseModel):
    pass

class SubjectCreate(SubjectBase):
    pass

class SubjectUpdate(BaseModel):
    pass

class SubjectRead(SubjectBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
