from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from backend.app.core.security import verify_access_token
from sqlalchemy.orm import Session
from backend.app.database.database import get_db
from backend.app.models.user import User


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Récupère l'utilisateur actuel à partir du token d'accès JWT.
    
    Args:
        token (str): Le token d'accès JWT qui depend de l'instance oauth2_scheme.
        db (Session): La session de base de données qui depend de la fonction get_db.

    Returns:
        dict: Les informations de l'utilisateur actuel en dictionnaire python.

    Raises:
        HTTPException: Si le token est invalide ou expiré une erreur est levée.
    """
    payload = verify_access_token(token)
    ExecptionRaise = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token d'accès invalide ou expiré",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if payload is None:
        raise ExecptionRaise
    
    user_id = payload.get("sub")
    if user_id is None:
        raise ExecptionRaise
      
    # Récupérer l'utilisateur à partir de la base de données en utilisant l'ID
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Utilisateur non trouvé",
        )
    
    return user