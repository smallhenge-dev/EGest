# Decision 001 - Separation Backend et Frontend

## Statut

Acceptee.

## Contexte

EGest doit etre une application de gestion capable d'evoluer dans le temps. Le projet doit pouvoir accueillir plusieurs modules metier sans melanger l'interface, la logique metier et l'acces aux donnees.

## Decision

Le projet est separe en deux parties principales :

- `backend/` pour l'API, la logique metier et les donnees ;
- `frontend/` pour l'application desktop et l'experience utilisateur.

Le backend expose une API FastAPI. Le frontend PySide6 communique avec cette API.

## Alternatives envisagees

### Application desktop monolithique

Toute la logique aurait pu etre directement placee dans l'application PySide6.

Avantage :

- plus rapide a prototyper au debut.

Inconvenients :

- plus difficile a tester ;
- logique metier melangee avec l'interface ;
- reutilisation plus compliquee si une interface web ou mobile arrive plus tard.

### API uniquement web

Le projet aurait pu etre concu uniquement comme une application web.

Avantage :

- deploiement centralise.

Inconvenients :

- ne correspond pas au choix actuel d'une application desktop ;
- demande une couche frontend web supplementaire.

## Consequences

- Le backend peut etre teste independamment.
- Le frontend reste concentre sur l'interface utilisateur.
- Les modules metier peuvent etre ajoutes plus proprement.
- Le projet pourra eventuellement accueillir d'autres interfaces plus tard.

