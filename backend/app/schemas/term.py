"""Sch?mas Pydantic pour les p?riodes scolaires."""

from typing import Optional

from pydantic import BaseModel, ConfigDict

class TermBase(BaseModel):
    pass

class TermCreate(TermBase):
    pass

class TermUpdate(BaseModel):
    pass

class TermRead(TermBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
