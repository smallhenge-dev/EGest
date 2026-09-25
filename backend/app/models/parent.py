from backend.app.database.database import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey


class Parent(Base):
    """
    Modèle représentant un parent dans la base de données.

    Attributs:
        id (int): L'identifiant unique du parent.
        user_id (int): L'identifiant de l'utilisateur associé au parent.
        first_name (str): Le prénom du parent.
        last_name (str): Le nom de famille du parent.
        email (str): L'adresse e-mail du parent.
        phone_number (str): Le numéro de téléphone du parent.
    """

    __tablename__ = "parents"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=True)


    # Définir la relation avec le modèle Student
    user: Mapped["User"] = relationship(back_populates="parent")
    parentStudent: Mapped["ParentStudent"] = relationship(back_populates="parent")
