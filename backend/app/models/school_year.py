from datetime import datetime, timezone
from backend.app.database.database import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column


from sqlalchemy import Integer, String, Boolean, DateTime


class SchoolYear(Base):
    """
    Modèle représentant une année scolaire dans la base de données.

    Attributs:
        id (int): L'identifiant unique de l'année scolaire.
        name (str): Le nom de l'année scolaire (par exemple, "2023-2024").
        start_date (datetime): La date de début de l'année scolaire.
        end_date (datetime): La date de fin de l'année scolaire.
        is_active (bool): Indique si l'année scolaire est active.
        created_at (datetime): La date et l'heure de création de l'année scolaire.
    """

    __tablename__ = "school_years"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    start_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc).replace(tzinfo=None))

    term: Mapped["Term"] = relationship(back_populates="school_year")
    classe: Mapped["Classe"] = relationship(back_populates="year")
    enroll: Mapped["Enrollment"] = relationship(back_populates="year")
    invoice: Mapped["Invoice"] = relationship(back_populates="year")
