"""Sch?mas Pydantic pour les paiements."""

from typing import Optional

from pydantic import BaseModel, ConfigDict

class PaymentBase(BaseModel):
    pass

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    pass

class PaymentRead(PaymentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
