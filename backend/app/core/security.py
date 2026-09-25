from datetime import datetime, timedelta, timezone
from typing import Any
import jwt
from passlib.context import CryptContext
from backend.app.core.config import settings

#mise en place de la configuration du contexte de hachage pour le mot de passe avec l'algorithme bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Verification du mot de passe en le comparant avec le mot de passe haché
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Vérifie si le mot de passe plat correspond au mot de passe haché.
    Args:
        plain_password (str): Le mot de passe en clair à vérifier.
        hashed_password (str): Le mot de passe haché à comparer.

    Returns:
        bool: True si le mot de passe correspond, False sinon. 
    """
    return pwd_context.verify(plain_password, hashed_password)

# Hachage du mot de passe afin de le stocker dans la base de données
def get_password_hash(password: str) -> str:
    """
    Hache le mot de passe en utilisant l'algorithme bcrypt.
    Args:
        password (str): Le mot de passe en clair à hacher.

    Returns:
        str: Le mot de passe haché.
    """
    return pwd_context.hash(password)

# Création du token d'accès JWT
def create_access_token(data: dict[str, Any], expires_delta: timedelta | None = None):
    """
    Crée un token d'accès JWT en utilisant les données fournies et une durée d'expiration optionnelle.
    Args:
        data (dict[str, Any]): Les données à inclure dans le payload du token.
        expires_delta (timedelta | None): La durée d'expiration du token. Si None, utilise la valeur par défaut.
        
    Returns:
        str: Le token d'accès JWT encodé.
        
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITH)
    print(settings.JWT_SECRET_KEY)
    return encoded_jwt

# Vérification du token d'accès JWT
def verify_access_token(token: str) -> dict | None:
    """
    Vérifie la validité du token d'accès JWT et retourne le payload décodé si le token est valide.
    Args:
        token (str): Le token d'accès JWT à vérifier.
        
    Returns:
        dict | None: Le payload décodé du token si le token est valide, sinon None.
    """
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITH])
        return payload
    except jwt.ExpiredSignatureError:
       return None

    except jwt.InvalidTokenError:
        return None