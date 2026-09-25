from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from collections.abc import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from backend.app.core.config import setting

"""

"""

class Base(DeclarativeBase):
    """
    ===================================================================
    classe de base, elle nous permet de presenter nos tables
    en Objet Python.
    ====================================================================
    """
    pass

class session():
    """
    ====================================================================
    creation de la session et acces a la base de donnee
    ====================================================================
    """
    def __init__(self):
        self.engine = create_async_engine(setting.DATABASE_URL,
                                    echo=setting.DEBUG,
                                    pool_pre_ping=True
                                    )
        self.sessionLocal = async_sessionmaker(bind=self.engine, class_=AsyncSession, expire_on_commit=False)

    async def get_db(self):
        """
        Session permanante a la base de donnees et offre un acces a l'API FastApi
        """
        async with self.sessionLocal() as db:
            try:
                yield db
            finally:
                await db.close()
    
