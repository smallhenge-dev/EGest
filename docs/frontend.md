# Frontend Desktop

Le frontend de EGest est une application desktop construite avec PySide6.

## Objectifs

- Proposer une interface claire et professionnelle.
- Faciliter les actions frequentes.
- Communiquer proprement avec l'API backend.
- Garder les composants reutilisables.

## Point d'entree

```text
frontend/app/main.py
```

## Organisation

```text
frontend/app/
  assets/
  components/
  core/
  layouts/
  models/
  screens/
  services/
  utils/
```

## Layout principal

Le layout principal pourra contenir :

- une barre laterale pour la navigation ;
- une barre superieure pour les actions globales ;
- une zone centrale pour l'ecran actif ;
- une barre de statut pour les informations systeme.

## Ecrans possibles

- Tableau de bord.
- Connexion.
- Utilisateurs.
- Clients.
- Produits ou services.
- Factures.
- Rapports.
- Parametres.

## Client API

Le fichier `frontend/app/core/api_client.py` devrait centraliser les appels HTTP vers le backend.

Objectif :

- eviter de disperser les appels API dans les ecrans ;
- gerer les erreurs de maniere uniforme ;
- ajouter facilement l'authentification plus tard.

## Sessions et permissions

Les fichiers suivants sont prevus pour gerer l'etat utilisateur :

- `auth_manager.py`
- `session.py`
- `permission.py`

Ils permettront de savoir qui est connecte, ce qu'il peut voir et ce qu'il peut modifier.

