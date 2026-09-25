from backend.app.database.database import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class AcademicLevel(Base):
    """
    Modele qui represente les niveau academique dans la base de donnees

    id[int]: l'identifiant unique du niveau
    name[str]: appelation du niveau
    code[str]: code representant le niveau academique
    description[str]: description
    """
    __tablename__ = "academic_levels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    code: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)

    classe: Mapped["Classe"] = relationship(back_populates="level")
    fee: Mapped["Fee"] = relationship(back_populates="level")
