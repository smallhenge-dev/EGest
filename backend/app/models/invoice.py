from backend.app.database.database import Base
from sqlalchemy import Date, Float, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


from datetime import date


class Invoice(Base):
    """
    id: identifiant unique de la facture
    student_id: identifiant unique de l'etudiant associe a la factur
    school_year_id: identifiant unique de l'annee scolaire associe a la facture
    invoice_number:
    issue_date:
    due_date:
    total_amount:
    status:

    """
    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))
    school_year_id: Mapped[int] = mapped_column(ForeignKey("school_years.id"))
    invoice_number: Mapped[int] = mapped_column(Integer, unique=True)
    issue_date: Mapped[date] = mapped_column(Date, unique=True)
    due_date: Mapped[date] = mapped_column(Date, unique=True)
    total_amount: Mapped[float] = mapped_column(Float, nullable=True)
    status: Mapped[str] = mapped_column(String, nullable=True)

    student: Mapped["Student"] = relationship(back_populates="invoice")
    year: Mapped["SchoolYear"] = relationship(back_populates="invoice")
    invoice_item: Mapped["InvoiceItem"] = relationship(back_populates="invoice")
    payment: Mapped["Payment"] = relationship(back_populates="invoice")
