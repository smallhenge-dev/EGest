"""Sch?mas Pydantic pour les parents."""

from typing import Optional

from pydantic import BaseModel, ConfigDict

class ParentBase(BaseModel):
    pass

class ParentCreate(ParentBase):
    pass

class ParentUpdate(BaseModel):
    pass

class ParentRead(ParentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
