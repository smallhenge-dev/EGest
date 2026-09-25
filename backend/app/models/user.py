from backend.app.database.database import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime, timezone


class User(Base):

    """
    Modèle représentant un utilisateur dans la base de données.

    Attributs:
        id (int): L'identifiant unique de l'utilisateur.
        username (str): Le nom d'utilisateur.
        email (str): L'adresse e-mail de l'utilisateur.
        hashed_password (str): Le mot de passe haché de l'utilisateur.
        role_id (int): L'identifiant du rôle de l'utilisateur.
        is_active (bool): Indique si l'utilisateur est actif.
        is_superuser (bool): Indique si l'utilisateur est un superutilisateur.
        created_at (datetime): La date et l'heure de création de l'utilisateur.
        updated_at (datetime): La date et l'heure de la dernière mise à jour de l'utilisateur.
    """

    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False) 
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc).replace(tzinfo=None))
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc).replace(tzinfo=None),
        onupdate=lambda: datetime.now(timezone.utc).replace(tzinfo=None),
    )

    parent: Mapped["Parent"] = relationship(back_populates="user")
    role: Mapped["Role"] = relationship(back_populates="user")
    student: Mapped["Student"] = relationship(back_populates="user")
    teacher: Mapped["Teacher"] = relationship(back_populates="user")
    payment: Mapped["Payment"] = relationship(back_populates="user")
    audit_logs: Mapped[list["AuditLog"]] = relationship(back_populates="user")
    sent_messages: Mapped[list["Message"]] = relationship(back_populates="sender", foreign_keys="[Message.sender_id]")
    received_messages: Mapped[list["Message"]] = relationship(back_populates="receiver", foreign_keys="[Message.receiver_id]")
    notifications: Mapped[list["Notification"]] = relationship(back_populates="user")
    documents: Mapped[list["Document"]] = relationship(back_populates="user")



class Role(Base):
    """
    Modèle représentant un rôle dans la base de données.

    Attributs:
        id (int): L'identifiant unique du rôle.
        name (str): Le nom du rôle.
        description (str): La description du rôle.
    """

    __tablename__ = "roles"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    description: Mapped[str] = mapped_column(String, nullable=True)

    user: Mapped[list["User"]] = relationship(back_populates="role")

class Permission(Base):
    """
    Modèle représentant une permission dans la base de données.

    Attributs:
        id (int): L'identifiant unique de la permission.
        name (str): Le nom de la permission.
        description (str): La description de la permission.
    """

    __tablename__ = "permissions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    description: Mapped[str] = mapped_column(String, nullable=True)
