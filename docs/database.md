# Base de Donnees

La couche base de donnees de EGest doit etre isolee dans `backend/app/database/`, avec les modeles dans `backend/app/models/` et les operations de lecture/ecriture dans `backend/app/repositories/`.

## Objectifs

- Centraliser la configuration de connexion.
- Eviter de melanger SQL, routes API et logique metier.
- Faciliter les tests.
- Preparer les migrations avec Alembic.

## Organisation recommandee

```text
backend/app/database/
  connection.py
  session.py

backend/app/models/
  user.py
  client.py
  invoice.py

backend/app/repositories/
  user_repository.py
  client_repository.py
  invoice_repository.py
```

## Role des modeles

Les modeles representent les tables de la base de donnees.

Exemples futurs :

- `User`
- `Role`
- `Client`
- `Product`
- `Invoice`
- `Payment`

## Role des repositories

Les repositories regroupent les operations sur les donnees.

Exemples :

- creer un utilisateur ;
- rechercher un client ;
- lister les factures ;
- mettre a jour un paiement.

## Migrations

Alembic servira a versionner les changements de schema de base de donnees.

Exemples de changements a migrer :

- ajout d'une table ;
- ajout d'une colonne ;
- changement d'un index ;
- creation d'une contrainte.

## Choix de base de donnees

Pendant le developpement, SQLite peut etre utile pour demarrer vite.

Pour une utilisation plus robuste, PostgreSQL est recommande.

