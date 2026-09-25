"""Sch?mas Pydantic pour les frais scolaires."""

from typing import Optional

from pydantic import BaseModel, ConfigDict

class FeeBase(BaseModel):
    pass

class FeeCreate(FeeBase):
    pass

class FeeUpdate(BaseModel):
    pass

class FeeRead(FeeBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
