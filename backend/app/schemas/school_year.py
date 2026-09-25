"""Sch?mas Pydantic pour les ann?es scolaires."""

from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class SchoolYearBase(BaseModel):
    name: str
    start_date: date
    end_date: date
    is_active: bool = True


class SchoolYearCreate(SchoolYearBase):
    pass


class SchoolYearUpdate(BaseModel):
    name: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    is_active: Optional[bool] = None


class SchoolYearRead(SchoolYearBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
