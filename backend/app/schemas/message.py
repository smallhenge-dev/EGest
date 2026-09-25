"""Sch?mas Pydantic pour les messages."""

from typing import Optional

from pydantic import BaseModel, ConfigDict

class MessageBase(BaseModel):
    pass

class MessageCreate(MessageBase):
    pass

class MessageUpdate(BaseModel):
    pass

class MessageRead(MessageBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
