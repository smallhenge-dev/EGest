from backend.app.database.database import Base
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Attendance(Base):
    """
    id:
    attendance_session_id:
    student_id:
    status:
    justification:
    comment:
    """

    __tablename__ = "attendances"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    attendance_session_id: Mapped[int] = mapped_column(ForeignKey("attendance_sessions.id"))
    student_id:  Mapped[int] = mapped_column(ForeignKey("students.id"))
    status: Mapped[str] = mapped_column(String, nullable=False)
    justification:  Mapped[str] = mapped_column(String, nullable=False)
    comment:  Mapped[str] = mapped_column(String, nullable=False)

    attendance_ses: Mapped["AttendanceSession"] = relationship(back_populates="attendance")
    student: Mapped["Student"] = relationship(back_populates="attendance")
