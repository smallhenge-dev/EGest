from backend.app.database.database import Base
from sqlalchemy import Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


from datetime import datetime, timezone

class Grade(Base):
    """
    Modele qui represente les notes des etudiants dans la base de donnees

    id: identifiant unique de la note
    student_id: identifiant unique de l'etudiant associe a la note
    subject_id: identifiant unique de la matiere associe a la note
    classe_id: identifiant unique de la classe associe a la note
    term_id: identifiant unique du trimesttre associee a la note
    teacher_id: identifiant unique de l'enseignant associe a la note
    value: contenaire de la note 
    assessment_type: type d'examen -> composition ou devoirs
    assessment_name: nom de l'examen
    assessment_date: date du deroulement de l'examen
    comment: commentaire sur la note
    created_at: heure d'insertion de la note
    updated_at: heure de la modification de la note
    """
    __tablename__ = "grades"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"))
    classe_id: Mapped[int] = mapped_column(ForeignKey("classes.id"))
    term_id: Mapped[int] = mapped_column(ForeignKey("terms.id"))
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"))
    value: Mapped[float] = mapped_column(Float, nullable=False)
    assessment_type: Mapped[str] = mapped_column(String, nullable=False)
    assessment_name: Mapped[str] = mapped_column(String, nullable=False)
    assessment_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    comment: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc).replace(tzinfo=None))
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc).replace(tzinfo=None),
        onupdate=lambda: datetime.now(timezone.utc).replace(tzinfo=None),
    )

    student: Mapped["Student"] = relationship(back_populates="grade")
    subject: Mapped["Subject"] = relationship(back_populates="grade")
    classe: Mapped["Classe"] = relationship(back_populates="grade")
    term: Mapped["Term"] = relationship(back_populates="grade")
    teacher: Mapped["Teacher"] = relationship(back_populates="grade")
