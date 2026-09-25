from backend.app.database.database import Base
from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone


class Teacher(Base):
    """
    Modèle représentant un enseignant dans la base de données.

    Attributs:
        id (int): L'identifiant unique de l'enseignant.
        user_id (int): L'identifiant de l'utilisateur associé à l'enseignant.
        matricule_employe (str): Le numéro de matricule unique de l'enseignant.
        hire_date (datetime): La date d'embauche de l'enseignant.
        specialization (str): La spécialisation de l'enseignant.
        qualifications (str): Les qualifications de l'enseignant.
        created_at (datetime): La date et l'heure de création de l'enseignant.
        updated_at (datetime): La date et l'heure de la dernière mise à jour de l'enseignant.
    """

    __tablename__ = "teachers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    matricule_employe: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    hire_date: Mapped[str] = mapped_column(String, nullable=False)
    specialization: Mapped[str] = mapped_column(String, nullable=True)
    qualifications: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc).replace(tzinfo=None))
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc).replace(tzinfo=None),
        onupdate=lambda: datetime.now(timezone.utc).replace(tzinfo=None),
    )

    # Définir la relation avec le modèle User
    user: Mapped["User"] = relationship(back_populates="teacher")
    teacherSub: Mapped["TeacherSubject"] = relationship(back_populates="teacher")
    grade: Mapped["Grade"] = relationship(back_populates="teacher")
    schedule: Mapped["Schedule"] = relationship(back_populates="teacher")
    attendance_ses: Mapped[list["AttendanceSession"]] = relationship(back_populates="teacher")
