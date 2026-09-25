from backend.app.database.database import Base
from sqlalchemy import Integer, String, ForeignKey, Date, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship


from datetime import timezone, time, date


class AttendanceSession(Base):
    """
    id: identifiant unique des seances de cours
    classe_id: identifiant unique de la classe dans leaquel se deroule le cours
    subject_id: identifiant unique de la matiere qui se deroule actuellement
    teacher_id: identifiant unique du professeur qui enseigne le cours
    schedule_id: identifiant unique de l'emploi du temps des cours
    session_date: date du cours
    start_time: heure du debut des cours
    end_time: heure finale des cours
    """

    __tablename__ = "attendance_sessions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    classe_id: Mapped[int] = mapped_column(ForeignKey("classes.id"))
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"))
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"))
    schedule_id: Mapped[int] = mapped_column(ForeignKey("shedules.id"))
    session_date: Mapped[date] = mapped_column(Date, nullable=False)
    start_time: Mapped[time] = mapped_column(Time, nullable=False)
    end_time: Mapped[time] = mapped_column(Time, nullable=False)

    attendance: Mapped[list["Attendance"]] = relationship(back_populates="attendance_ses")
    classe: Mapped["Classe"] = relationship(back_populates="attendance_ses")
    subject: Mapped["Subject"] = relationship(back_populates="attendance_ses")
    teacher: Mapped["Teacher"] = relationship(back_populates="attendance_ses")
    schedule: Mapped["Schedule"] = relationship(back_populates="attendance_ses")
