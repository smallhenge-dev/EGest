from backend.app.database.database import Base
from sqlalchemy import Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


from datetime import datetime, timezone


class Report(Base):
    """
    id: identifiant unique du bulletin 
    student_id: identifiant unique de l'eleve associe a son bulletin
    classe_id: identifiant unique de la classe associe au bulletin
    term_id: identifiant unique du trimestre associe au bulletin
    general_average: Moyenne generale de toutes les notes de l'eleve
    rank: rang de l'eleve
    appreciation: apprecation de l'eleve par le professeur pricipal
    decision: decision finale, dire si l'eleve est: admis, echoue
    generated_at: date de la creation du bulletin
    pdf_url: url du bulletin
    """
    __tablename__ = "reports"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), unique=True)
    classe_id: Mapped[int] = mapped_column(ForeignKey("classes.id"), unique=True)
    term_id: Mapped[int] = mapped_column(ForeignKey("terms.id"), unique=True)
    general_average: Mapped[float] = mapped_column(Float, nullable=False)
    rank: Mapped[int] = mapped_column(Integer, nullable=False)
    appreciation: Mapped[str] = mapped_column(String, nullable=True)
    decision: Mapped[str] = mapped_column(String, nullable=False)
    generated_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc).replace(tzinfo=None))
    pdf_url: Mapped[str] = mapped_column(String, nullable=True)

    student: Mapped["Student"] = relationship(back_populates="report")
    classe: Mapped["Classe"] = relationship(back_populates="report")
    term: Mapped["Term"] = relationship(back_populates="report")
