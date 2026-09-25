"""Sch?mas Pydantic pour les lignes de facture."""

from typing import Optional

from pydantic import BaseModel, ConfigDict

class InvoiceItemBase(BaseModel):
    pass

class InvoiceItemCreate(InvoiceItemBase):
    pass

class InvoiceItemUpdate(BaseModel):
    pass

class InvoiceItemRead(InvoiceItemBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
