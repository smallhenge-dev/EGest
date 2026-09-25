from backend.app.database.database import Base
from sqlalchemy import Date, Float, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


from datetime import date


class Payment(Base):
    """
    id: Unique identifier for the payment.
    invoice_id: Identifier of the invoice associated with the payment.
    student_id: Identifier of the student associated with the payment.
    received_by: Identifier of the user who received the payment.
    amount: The amount of the payment.
    payment_date: The date when the payment was made.
    payment_method: The method used for the payment.
    transaction_ref: The reference for the transaction.
    status: The status of the payment.
    """
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    invoice_id: Mapped[int] = mapped_column(ForeignKey("invoices.id"))
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))
    received_by: Mapped[int] = mapped_column(ForeignKey("users.id"))
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    payment_date: Mapped[date] = mapped_column(Date, unique=True)
    payment_method: Mapped[str] = mapped_column(String, unique=True)
    transaction_ref: Mapped[str] = mapped_column(String, unique=True)
    status: Mapped[str] = mapped_column(String, unique=True)
    
    invoice: Mapped["Invoice"] = relationship(back_populates="payment")
    student: Mapped["Student"] = relationship(back_populates="payment")
    user: Mapped["User"] = relationship(back_populates="payment")
