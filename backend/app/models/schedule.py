from backend.app.database.database import Base
from sqlalchemy import Integer, String, Time, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


from datetime import time


class Schedule(Base):
    """
    id: identifiant unique de l'emploi du temps
    classe_id: identifiant unique de la classe associe a l'emploi du temps
    subject_id: identifiant unique de la matiere associe a lemploi du temps
    teacher_id: identifiant unique du professeur associe a l'emploi du temps
    day_of_week: differents jours de la semaine
    sart_time: debut du cours
    end_time: fin du cours
    room: 
    """

    __tablename__ = "shedules"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    classe_id: Mapped[int] = mapped_column(ForeignKey("classes.id"))
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"))
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"))
    day_of_week: Mapped[str] = mapped_column(String, nullable=False)
    sart_time: Mapped[time] = mapped_column(Time, nullable=False)
    end_time: Mapped[time] = mapped_column(Time, nullable=False)
    room: Mapped[str] = mapped_column(String, nullable=False)

    classe: Mapped["Classe"] = relationship(back_populates="schedule")
    subject: Mapped["Subject"] = relationship(back_populates="schedule")
    teacher: Mapped["Teacher"] = relationship(back_populates="schedule")
    attendance_ses: Mapped[list["AttendanceSession"]] = relationship(back_populates="schedule")
