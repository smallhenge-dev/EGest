from datetime import datetime, timezone
from sqlalchemy import Boolean, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.app.database.database import Base


class Student(Base):
    """
    Modèle représentant un étudiant dans la base de données.

    Attributs:
        id (int): L'identifiant unique de l'étudiant.
        user_id (int): L'identifiant de l'utilisateur associé à l'étudiant.
        matricule (str): Le numéro de matricule unique.
        first_name (str): Le nom de l'étudiant.
        last_name (str): Le prénom de l'étudiant.
        date_of_birth (datetime): La date de naissance de l'étudiant.
        place_of_birth (str): Le lieu de naissance de l'étudiant.
        gender (str): Le genre de l'étudiant (par exemple, "M" pour
    masculin, "F" pour féminin).
        phone_number (str): Le numéro de téléphone de l'étudiant.
        address (str): L'adresse de l'étudiant.
        photo_url (str): L'URL de la photo de l'étudiant.
        status (str): Le statut de l'étudiant (par exemple, "actif", "inactif").
        email (str): L'adresse e-mail de l'étudiant.
        is_active (bool): Indique si l'étudiant est actif.
        created_at (datetime): La date et l'heure de création de l'étudiant.
        updated_at (datetime): La date et l'heure de la dernière mise à jour de l'étudiant.
    """

    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    matricule: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    date_of_birth: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    place_of_birth: Mapped[str] = mapped_column(String, nullable=False)
    gender: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=True)
    address: Mapped[str] = mapped_column(String, nullable=True)
    photo_url: Mapped[str] = mapped_column(String, nullable=True)
    status: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc).replace(tzinfo=None))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc).replace(tzinfo=None),
        onupdate=lambda: datetime.now(timezone.utc).replace(tzinfo=None),
    )

    user: Mapped["User"] = relationship(back_populates="student")
    enroll: Mapped[list["Enrollment"]] = relationship(
        back_populates="student",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    grade: Mapped["Grade"] = relationship(back_populates="student")
    report: Mapped["Report"] = relationship(back_populates="student")
    invoice: Mapped["Invoice"] = relationship(back_populates="student")
    payment: Mapped["Payment"] = relationship(back_populates="student")
    parentStudent: Mapped["ParentStudent"] = relationship(back_populates="student")
    attendance: Mapped[list["Attendance"]] = relationship(back_populates="student")
    documents: Mapped[list["Document"]] = relationship(back_populates="student")
