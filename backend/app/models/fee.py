from backend.app.database.database import Base
from sqlalchemy import Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


from datetime import datetime, timezone


class Fee(Base):
    """
    id: identifiant unique des frais scolaire
    academic_level_id: identifiant unique du niveau academique associe au frais
    name: type de frais: scolaire, inscription, examen, document
    description: description des frai
    amount: montant paye 
    frequency: la periodicite du paiement-> mensuel, trimestre, semestre, annuel
    is_riquired: un booleen indiquant si le paiementest obligatoire (True) ou optionel (False)
    status: etat confirmant le paiement: paye, reste
    created_at: date et heure auxquelles l'enregistrement a ete cree dans la base de donnees
    """

    __tablename__ = "fees"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    academic_level_id: Mapped[int] = mapped_column(ForeignKey("academic_levels.id"))
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    frequency: Mapped[str] = mapped_column(String, nullable=False)
    is_riquired: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc).replace(tzinfo=None))

    level: Mapped["AcademicLevel"] = relationship(back_populates="fee")
    invoice_item: Mapped["InvoiceItem"] = relationship(back_populates="fee")
