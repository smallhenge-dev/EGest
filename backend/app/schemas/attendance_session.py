"""Sch?mas Pydantic pour les sessions de pr?sence."""

from typing import Optional

from pydantic import BaseModel, ConfigDict

class AttendanceSessionBase(BaseModel):
    pass

class AttendanceSessionCreate(AttendanceSessionBase):
    pass

class AttendanceSessionUpdate(BaseModel):
    pass

class AttendanceSessionRead(AttendanceSessionBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
