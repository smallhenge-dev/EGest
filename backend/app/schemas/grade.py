"""Sch?mas Pydantic pour les notes."""

from typing import Optional

from pydantic import BaseModel, ConfigDict

class GradeBase(BaseModel):
    pass

class GradeCreate(GradeBase):
    pass

class GradeUpdate(BaseModel):
    pass

class GradeRead(GradeBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
