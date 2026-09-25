"""Sch?mas Pydantic pour les enseignants."""

from typing import Optional

from pydantic import BaseModel, ConfigDict

class TeacherBase(BaseModel):
    pass

class TeacherCreate(TeacherBase):
    pass

class TeacherUpdate(BaseModel):
    pass

class TeacherRead(TeacherBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
