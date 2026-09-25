"""Sch?mas Pydantic pour les niveaux acad?miques."""

from typing import Optional

from pydantic import BaseModel, ConfigDict


class AcademicLevelBase(BaseModel):
    name: str
    code: str
    description: str


class AcademicLevelCreate(AcademicLevelBase):
    pass


class AcademicLevelUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None


class AcademicLevelRead(AcademicLevelBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
