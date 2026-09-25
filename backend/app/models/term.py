from backend.app.database.database import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, String, Boolean, DateTime


class Term(Base):
    """
    Modèle représentant un trimestre dans la base de données.

    Attributs:
        id (int): L'identifiant unique du trimestre.
        name (str): Le nom du trimestre (par exemple, "Trimestre 1").
        start_date (datetime): La date de début du trimestre.
        end_date (datetime): La date de fin du trimestre.
        positive (bool): Indique si le trimestre est actif.
        school_year_id (int): L'identifiant de l'année scolaire associée au trimestre.
    """

    __tablename__ = "terms"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    start_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    positive: Mapped[bool] = mapped_column(Boolean, default=False)
    school_year_id: Mapped[int] = mapped_column(Integer, ForeignKey("school_years.id"), nullable=False)

    school_year: Mapped["SchoolYear"] = relationship(back_populates="term")
    grade: Mapped["Grade"] = relationship(back_populates="term")
    report: Mapped["Report"] = relationship(back_populates="term")
