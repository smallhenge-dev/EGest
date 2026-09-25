from backend.app.database.database import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Subject(Base):
    """
    Modele qui represente toutes les matieres dans la base de donnees
    
    id: identifiant unique de la matiere
    code: codification de la matiere
    description: description de chaque matiere
    coefficient: coefficient de chaque matiere
    """
    __tablename__="subjects"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
    code: Mapped[str] = mapped_column(String, unique=True)
    description: Mapped[str] = mapped_column(String, nullable=False)
    coefficient: Mapped[int] = mapped_column(Integer, nullable=True)

    classeSub: Mapped["ClasseSubject"] = relationship(back_populates="subject")
    teacherSub: Mapped["TeacherSubject"] = relationship(back_populates="subject")
    grade: Mapped["Grade"] = relationship(back_populates="subject")
    schedule: Mapped["Schedule"] = relationship(back_populates="subject")
    attendance_ses: Mapped[list["AttendanceSession"]] = relationship(back_populates="subject")
