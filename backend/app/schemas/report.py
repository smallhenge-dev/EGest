"""Sch?mas Pydantic pour les rapports."""

from typing import Optional

from pydantic import BaseModel, ConfigDict

class ReportBase(BaseModel):
    pass

class ReportCreate(ReportBase):
    pass

class ReportUpdate(BaseModel):
    pass

class ReportRead(ReportBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
