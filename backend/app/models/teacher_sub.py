from backend.app.database.database import Base
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class TeacherSubject(Base):
    """
    id: identifiant unique de la matiere enseignee par cet enseignant
    classe_id: identifiant unique de la classe a laquelle la matiere est enseignee
    teacher_id: identifiant unique de l'enseignant qui enseigne cette matiere
    """

    __tablename__ = "teacher_subjects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    classe_id: Mapped[int] = mapped_column(ForeignKey("classes.id"))
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"))
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"))

    classe: Mapped["Classe"] = relationship(back_populates="teacherSub")
    teacher: Mapped["Teacher"] = relationship(back_populates="teacherSub")
    subject: Mapped["Subject"] = relationship(back_populates="teacherSub")
