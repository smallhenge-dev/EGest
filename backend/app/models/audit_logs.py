from backend.app.database.database import Base
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class AuditLog(Base):

    """
    Represents an audit log entry in the database.
    id: Unique identifier for the audit log entry.
    user_id: Identifier of the user who performed the action.
    action: Description of the action performed.
    timestamp: Date and time when the action was performed.
    
    """
    __tablename__ = "audit_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    action: Mapped[str] = mapped_column(String(255), nullable=False)
    timestamp: Mapped[DateTime] = mapped_column(DateTime, nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="audit_logs")
