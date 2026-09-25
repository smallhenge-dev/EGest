"""Sch?mas Pydantic pour les factures."""

from typing import Optional

from pydantic import BaseModel, ConfigDict

class InvoiceBase(BaseModel):
    pass

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceUpdate(BaseModel):
    pass

class InvoiceRead(InvoiceBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
