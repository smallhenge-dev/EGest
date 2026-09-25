"""Sch?mas Pydantic pour les classes."""

from typing import Optional

from pydantic import BaseModel, ConfigDict


class ClasseBase(BaseModel):
    academic_level_id: int
    school_year_id: int
    name: str
    code: str
    capacity: int


class ClasseCreate(ClasseBase):
    pass


class ClasseUpdate(BaseModel):
    academic_level_id: Optional[int] = None
    school_year_id: Optional[int] = None
    name: Optional[str] = None
    code: Optional[str] = None
    capacity: Optional[int] = None


class ClasseRead(ClasseBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
