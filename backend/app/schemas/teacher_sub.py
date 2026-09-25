"""Sch?mas Pydantic pour les relations enseignant-mati?re."""

from typing import Optional

from pydantic import BaseModel, ConfigDict

class TeacherSubjectBase(BaseModel):
    pass

class TeacherSubjectCreate(TeacherSubjectBase):
    pass

class TeacherSubjectUpdate(BaseModel):
    pass

class TeacherSubjectRead(TeacherSubjectBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
