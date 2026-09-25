from backend.app.database.database import Base
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Classe(Base):
    """
    id[int]: l'identifiant unique de la classe
    academic_level_id[int]: l'identifiant de academic_level associe a la classe
    school_year_id[int]: l'identifiant de l'annee scolaire associe a la classe
    name[str]: nom de classe
    code[str]: code d'appelation de la clsse
    capacity[int]: le nombre total de place dans la classe
    """

    __tablename__ = "classes"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    academic_level_id: Mapped[int] = mapped_column(ForeignKey("academic_levels.id"), nullable=False)
    school_year_id: Mapped[int] = mapped_column(ForeignKey("school_years.id"), nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    code: Mapped[str] = mapped_column(String, nullable=False)
    capacity: Mapped[int] = mapped_column(Integer, nullable=False)

    year: Mapped["SchoolYear"] = relationship(back_populates="classe")
    level: Mapped["AcademicLevel"] = relationship(back_populates="classe")
    enroll: Mapped["Enrollment"] = relationship(back_populates="classe")
    classeSub: Mapped["ClasseSubject"] = relationship(back_populates="classe")
    teacherSub: Mapped["TeacherSubject"] = relationship(back_populates="classe")
    grade: Mapped["Grade"] = relationship(back_populates="classe")
    report: Mapped["Report"] = relationship(back_populates="classe")
    schedule: Mapped["Schedule"] = relationship(back_populates="classe")
    attendance_ses: Mapped[list["AttendanceSession"]] = relationship(back_populates="classe")
