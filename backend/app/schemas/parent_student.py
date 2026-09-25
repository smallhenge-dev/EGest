"""Sch?mas Pydantic pour les relations parent-?l?ve."""

from typing import Optional

from pydantic import BaseModel, ConfigDict

class ParentStudentBase(BaseModel):
    pass

class ParentStudentCreate(ParentStudentBase):
    pass

class ParentStudentUpdate(BaseModel):
    pass

class ParentStudentRead(ParentStudentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
