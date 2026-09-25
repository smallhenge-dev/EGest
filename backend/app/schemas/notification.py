"""Sch?mas Pydantic pour les notifications."""

from typing import Optional

from pydantic import BaseModel, ConfigDict

class NotificationBase(BaseModel):
    pass

class NotificationCreate(NotificationBase):
    pass

class NotificationUpdate(BaseModel):
    pass

class NotificationRead(NotificationBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
