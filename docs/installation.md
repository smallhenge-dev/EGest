# Installation

Cette page decrit comment installer et lancer EGest en environnement de developpement.

## Prerequis

- Python 3.12 ou plus recent.
- Git.
- Un terminal PowerShell sous Windows.

## Creer l'environnement virtuel

```powershell
python -m venv .venv
```

## Activer l'environnement

```powershell
.\.venv\Scripts\Activate.ps1
```

Si le projet utilise encore le dossier `.env` comme environnement virtuel local :

```powershell
.\.env\Scripts\Activate.ps1
```

## Installer les dependances

```powershell
python -m pip install -r requirements.txt
```

## Lancer le backend

```powershell
uvicorn backend.app.main:app --reload
```

Verifier que l'API repond :

```text
http://127.0.0.1:8000/health
```

Documentation interactive :

```text
http://127.0.0.1:8000/docs
```

## Lancer le frontend

```powershell
python -m frontend.app.main
```

## Lancer les tests

```powershell
pytest
```

Ou avec l'environnement local existant :

```powershell
.\.env\Scripts\python.exe -m pytest
```

## Problemes frequents

### `ModuleNotFoundError`

Les dependances ne sont probablement pas installees dans l'environnement Python actif.

Solution :

```powershell
python -m pip install -r requirements.txt
```

### PowerShell bloque l'activation

Si PowerShell bloque le script d'activation, verifier la politique d'execution locale.

### Le backend ne demarre pas

Verifier que FastAPI et Uvicorn sont bien installes.

```powershell
python -m pip show fastapi uvicorn
```

