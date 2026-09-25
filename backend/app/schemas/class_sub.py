"""Sch?mas Pydantic pour les relations classe-mati?re."""

from typing import Optional

from pydantic import BaseModel, ConfigDict

class ClasseSubjectBase(BaseModel):
    pass

class ClasseSubjectCreate(ClasseSubjectBase):
    pass

class ClasseSubjectUpdate(BaseModel):
    pass

class ClasseSubjectRead(ClasseSubjectBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
