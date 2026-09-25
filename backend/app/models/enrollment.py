from backend.app.database.database import Base
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


from datetime import datetime, timezone


class Enrollment(Base):
    """
    id: identifiant unique de l'enrollement
    student_id: identifiant unique de l'etudiant associe a l'enrollement
    classe_id: identifiant unique de la classe associe a l'etudiant
    enrollment_date: date de paiement de l'etudiant
    status: status de l'etudiant (paye, en attente, reste, impaye)
    resgistration_number: numero sous lequel l'etudiant a effectue le paiement
    """
    __tablename__ = "enrollments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id", ondelete="CASCADE"), nullable=False)
    classe_id: Mapped[int] = mapped_column(ForeignKey("classes.id"), nullable=False)
    school_year_id: Mapped[int] = mapped_column(ForeignKey("school_years.id"), nullable=False)
    enrollment_date: Mapped[DateTime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc).replace(tzinfo=None))
    status: Mapped[str] = mapped_column(String, nullable=False)
    resgistration_number: Mapped[int] = mapped_column(Integer, nullable=False)

    year: Mapped["SchoolYear"] = relationship(back_populates="enroll", passive_deletes=True)
    student: Mapped["Student"] = relationship(back_populates="enroll", passive_deletes=True)
    classe: Mapped["Classe"] = relationship(back_populates="enroll")
