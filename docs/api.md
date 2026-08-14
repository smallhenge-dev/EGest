# API Backend

Le backend de EGest expose une API FastAPI.

## Point d'entree

```text
backend/app/main.py
```

## Endpoints actuels

### `GET /`

Retourne un message de bienvenue.

Reponse attendue :

```json
{
  "message": "Bienvenue sur l'API EGest"
}
```

### `GET /health`

Permet de verifier que l'API est disponible.

Reponse attendue :

```json
{
  "status": "ok"
}
```

## Documentation interactive

Une fois le backend lance, FastAPI expose automatiquement :

```text
http://127.0.0.1:8000/docs
```

## Organisation future des routes

Les routes devraient etre regroupees par domaine metier.

Exemple :

```text
backend/app/api/
  auth.py
  users.py
  clients.py
  invoices.py
  reports.py
```

## Convention recommandee

Chaque route doit rester fine :

- recevoir la requete ;
- valider les donnees ;
- appeler un service ;
- retourner une reponse claire.

La logique metier doit rester dans `services/`, pas directement dans les endpoints.

