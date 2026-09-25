from backend.app.database.database import Base
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class ClasseSubject(Base):
    """
    id: identifiant unique des matières enseignées
    class_id: identifiant unique des classes
    subject_id: identifiant unique des matières
    hours_per_week: Nombre des heures de matière enseignée par semaine
    """

    __tablename__ = "class_subjects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    class_id: Mapped[int] = mapped_column(ForeignKey("classes.id"))
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"))
    hours_per_week: Mapped[int] = mapped_column(Integer, nullable=False)

    classe: Mapped["Classe"] = relationship(back_populates="classeSub")
    subject: Mapped["Subject"] = relationship(back_populates="classeSub")
