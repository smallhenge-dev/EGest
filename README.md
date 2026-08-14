# EGest

EGest est une application de gestion des etablissements scolaires modernes construite autour d'une API FastAPI et d'une interface desktop PySide6.

Le projet vise a fournir une base claire, maintenable et evolutive pour gerer les operations essentielles d'une ecole : utilisateurs, donnees metier, tableaux de bord, rapports, exports et automatisations.

## Objectifs

- Centraliser les donnees de gestion dans une application simple a utiliser.
- Separer proprement l'interface utilisateur, l'API, la logique metier et l'acces aux donnees.
- Construire une base technique robuste pour ajouter progressivement des modules metier.
- Garder un projet lisible, testable et facile a faire evoluer.

## Technologies

- Python
- FastAPI pour le backend
- PySide6 pour l'application desktop
- SQLAlchemy pour la couche base de donnees
- Alembic pour les migrations
- Pydantic pour la validation des donnees
- Pytest pour les tests automatises

## Architecture

```text
EGest/
  backend/
    app/
      api/             Routes HTTP et endpoints FastAPI
      core/            Configuration, securite, constantes globales
      database/        Connexion, sessions et configuration base de donnees
      models/          Modeles SQLAlchemy
      repositories/    Acces aux donnees
      schemas/         Schemas Pydantic
      services/        Logique metier
      tasks/           Taches planifiees ou traitements asynchrones
      utils/           Fonctions utilitaires
      main.py          Point d'entree de l'API
    tests/             Tests du backend

  frontend/
    app/
      assets/          Images, logos et ressources graphiques
      components/      Composants reutilisables de l'interface
      core/            Session, permissions, routes, client API
      layouts/         Fenetre principale, sidebar, topbar, statusbar
      models/          Modeles utilises par l'interface
      screens/         Ecrans principaux de l'application
      services/        Services frontend
      utils/           Fonctions utilitaires frontend
      main.py          Point d'entree de l'application desktop
    tests/             Tests du frontend

  docs/                Documentation du projet
```

## Installation

Creer un environnement virtuel :

```powershell
python -m venv .venv
```

Activer l'environnement :

```powershell
.\.venv\Scripts\Activate.ps1
```

Installer les dependances :

```powershell
python -m pip install -r requirements.txt
```

## Lancer le backend

```powershell
uvicorn backend.app.main:app --reload
```

L'API est disponible a l'adresse :

```text
http://127.0.0.1:8000
```

Endpoint de verification :

```text
http://127.0.0.1:8000/health
```

Documentation interactive FastAPI :

```text
http://127.0.0.1:8000/docs
```

## Lancer le frontend

```powershell
python -m frontend.app.main
```

## Tests

Lancer tous les tests :

```powershell
pytest
```

Avec l'environnement local existant du projet :

```powershell
.\.env\Scripts\python.exe -m pytest
```

## Etat actuel

Le projet contient actuellement :

- Une structure backend prete pour une API FastAPI.
- Une structure frontend prete pour une application desktop PySide6.
- Un endpoint backend de verification `/health`.
- Une fenetre frontend minimale.
- Des tests de base pour valider que le projet demarre correctement.

## Roadmap

- Ajouter la configuration applicative centralisee.
- Connecter une base de donnees.
- Mettre en place les premiers modeles metier.
- Ajouter l'authentification et la gestion des sessions.
- Construire les premiers ecrans de l'application.
- Ajouter les roles et permissions.
- Integrer les exports PDF ou Excel.
- Renforcer la couverture de tests.

## Conventions

- Garder la logique metier dans `services/`.
- Garder l'acces aux donnees dans `repositories/`.
- Garder les schemas de validation dans `schemas/`.
- Garder les composants d'interface reutilisables dans `frontend/app/components/`.
- Ajouter des tests pour chaque fonctionnalite importante.

## Auteur

EGest est developpe comme une base d'application de gestion professionnelle, avec une attention particuliere portee a la clarte du code, a la maintenabilite et a l'evolution progressive du produit.
