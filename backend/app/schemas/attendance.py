"""Sch?mas Pydantic pour les pr?sences."""

from typing import Optional

from pydantic import BaseModel, ConfigDict

class AttendanceBase(BaseModel):
    pass

class AttendanceCreate(AttendanceBase):
    pass

class AttendanceUpdate(BaseModel):
    pass

class AttendanceRead(AttendanceBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
