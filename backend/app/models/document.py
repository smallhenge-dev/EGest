from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.database.database import Base


class Document(Base):
    """
    Modèle représentant un document lié à un utilisateur ou à un étudiant.
    id: Identifiant unique du document.
    user_id: Identifiant de l'utilisateur associé au document (nullable).
    student_id: Identifiant de l'étudiant associé au document (nullable).
    document_type: Type du document (ex: "pdf", "image", etc.).
    name: Nom du document.
    file_url: URL du fichier stocké.
    file_size: Taille du fichier en octets (nullable).
    mime_type: Type MIME du fichier (nullable).
    uploaded_at: Date et heure de l'upload du document (par défaut à la date actuelle).
    """

    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"), nullable=True)
    student_id: Mapped[int | None] = mapped_column(ForeignKey("students.id"), nullable=True)
    document_type: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    file_url: Mapped[str] = mapped_column(String, nullable=False)
    fille_size: Mapped[int | None] = mapped_column(Integer, nullable=True)
    mime_type: Mapped[str | None] = mapped_column(String, nullable=True)
    uploade_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc).replace(tzinfo=None))

    user: Mapped["User"] = relationship(back_populates="documents")
    student: Mapped["Student"] = relationship(back_populates="documents")
