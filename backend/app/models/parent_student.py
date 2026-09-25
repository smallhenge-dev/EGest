from backend.app.database.database import Base
from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class ParentStudent(Base):
    """
    id: Unique identifier for the parent-student relationship.
    parent_id: Identifier of the parent.
    student_id: Identifier of the student.
    relationship: Description of the relationship between the parent and student.
    is_primary: Indicates if the relationship is primary.   
    """

    __tablename__ = "Parent_students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey("parents.id"))
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))
    relationships: Mapped[str] = mapped_column(String, nullable=False)
    is_primary: Mapped[bool] = mapped_column(Boolean, nullable=False)

    parent: Mapped["Parent"] = relationship(back_populates="parentStudent")
    student: Mapped["Student"] = relationship(back_populates="parentStudent")
