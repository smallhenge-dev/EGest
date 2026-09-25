from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Setting(BaseSettings):
    """
    Paramètres de configuration de l'application.
    Les valeurs par défaut assurent un démarrage local/Swagger sans
    dépendre d'un .env présent dans l'environnement de test.
    """

    APP_NAME: str = "EGest API"
    APP_VERSION: str = "1.0.0"
    ENVIRONEMENT: str = "development"
    DEBUG: bool = False
    DATABASE_URL: str = "postgresql+asyncpg://postgres:EGest_2026-2027@localhost:5432/egest"
    JWT_SECRET_KEY: str = "change-me-in-production"
    JWT_ALGORITH: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).resolve().parents[2] / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

@lru_cache
def get_settings() -> Setting:
    """
    Récupère les paramètres de configuration de l'application à partir de .env si disponible.
    Sinon, renvoie les valeurs de secours du système local pour ne pas bloquer l'import.
    """
    return Setting()


setting = get_settings()
settings = setting

