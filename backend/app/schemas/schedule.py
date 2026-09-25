"""Sch?mas Pydantic pour les emplois du temps."""

from typing import Optional

from pydantic import BaseModel, ConfigDict

class ScheduleBase(BaseModel):
    pass

class ScheduleCreate(ScheduleBase):
    pass

class ScheduleUpdate(BaseModel):
    pass

class ScheduleRead(ScheduleBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
