from backend.app.database.database import Base
from sqlalchemy import Float, Integer, String, ForeignKey   
from sqlalchemy.orm import Mapped, mapped_column, relationship

class InvoiceItem(Base):
    """
    Represents an item in an invoice.
    id: Unique identifier for the invoice item.
    invoice_id: Identifier of the associated invoice.
    description: Description of the item.
    quantity: Quantity of the item.
    unit_price: Unit price of the item.
    total_price: Total price for the item (quantity * unit_price).
    """
    
    __tablename__ = "invoice_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    invoice_id: Mapped[int] = mapped_column(ForeignKey("invoices.id"), nullable=False)
    fee_id: Mapped[int] = mapped_column(ForeignKey("fees.id"), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    quantity: Mapped[float] = mapped_column(Float, nullable=False)
    unit_price: Mapped[float] = mapped_column(Float, nullable=False)
    total_price: Mapped[float] = mapped_column(Float, nullable=False)

    invoice: Mapped["Invoice"] = relationship("Invoice", back_populates="invoice_item")
    fee: Mapped["Fee"] = relationship(back_populates="invoice_item")
    fee: Mapped["Fee"] = relationship(back_populates="invoice_item")