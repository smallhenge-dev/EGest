# Architecture

EGest est organise en deux grandes parties :

- `backend/` : API, logique metier, donnees et services.
- `frontend/` : application desktop, ecrans, composants et communication avec l'API.

Cette separation permet de faire evoluer l'interface sans melanger le code utilisateur avec la logique metier et la base de donnees.

## Vue globale

```text
frontend desktop
      |
      | requetes HTTP
      v
backend FastAPI
      |
      | services metier
      v
repositories
      |
      | SQLAlchemy
      v
base de donnees
```

## Backend

Le backend est construit autour de FastAPI.

```text
backend/
  app/
    api/
    core/
    database/
    models/
    repositories/
    schemas/
    services/
    tasks/
    utils/
    main.py
  tests/
```

### `api/`

Contient les routes HTTP exposees par l'application.

Exemples futurs :

- `api/users.py`
- `api/auth.py`
- `api/clients.py`
- `api/reports.py`

### `core/`

Contient les elements transversaux :

- configuration globale ;
- securite ;
- constantes ;
- gestion des erreurs communes.

### `database/`

Contient la configuration de la base de donnees :

- moteur SQLAlchemy ;
- sessions ;
- dependances FastAPI ;
- configuration Alembic.

### `models/`

Contient les modeles SQLAlchemy qui representent les tables.

### `schemas/`

Contient les schemas Pydantic utilises pour valider les donnees qui entrent et sortent de l'API.

### `repositories/`

Contient l'acces aux donnees. Les repositories savent comment lire et ecrire dans la base, mais ne portent pas la logique metier principale.

### `services/`

Contient la logique metier. C'est ici que les regles importantes de l'application doivent vivre.

### `tasks/`

Contient les traitements planifies ou longs :

- generation de rapports ;
- exports ;
- synchronisations ;
- nettoyages automatiques.

### `utils/`

Contient les fonctions utilitaires generales.

## Frontend

Le frontend est une application desktop PySide6.

```text
frontend/
  app/
    assets/
    components/
    core/
    layouts/
    models/
    screens/
    services/
    utils/
    main.py
  tests/
```

### `assets/`

Images, logos, icones et ressources graphiques.

### `components/`

Composants reutilisables de l'interface :

- boutons ;
- cartes ;
- tableaux ;
- formulaires ;
- boites de dialogue.

### `core/`

Elements centraux du frontend :

- client API ;
- session utilisateur ;
- permissions ;
- navigation ;
- authentification.

### `layouts/`

Structure principale de l'application :

- fenetre principale ;
- barre laterale ;
- barre superieure ;
- barre de statut.

### `screens/`

Ecrans principaux visibles par l'utilisateur.

### `services/`

Services frontend qui appellent l'API ou orchestrent certaines actions de l'interface.

## Regle importante

Une fonctionnalite complete doit generalement traverser ces couches :

```text
screen -> service frontend -> API -> service backend -> repository -> database
```

Cette discipline evite que le code devienne difficile a maintenir.

