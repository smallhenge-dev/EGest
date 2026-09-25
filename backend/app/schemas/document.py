"""Sch?mas Pydantic pour les documents."""

from typing import Optional

from pydantic import BaseModel, ConfigDict

class DocumentBase(BaseModel):
    pass

class DocumentCreate(DocumentBase):
    pass

class DocumentUpdate(BaseModel):
    pass

class DocumentRead(DocumentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
