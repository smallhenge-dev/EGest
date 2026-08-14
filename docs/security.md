# Securite

La securite doit etre prise en compte des le debut du projet, meme si toutes les fonctionnalites ne sont pas encore implementees.

## Objectifs

- Proteger les comptes utilisateurs.
- Controler les acces aux modules.
- Eviter l'exposition des secrets.
- Valider toutes les donnees entrantes.
- Garder une trace des actions importantes.

## Authentification

Le backend devra gerer :

- connexion ;
- deconnexion ;
- expiration de session ;
- renouvellement de token si necessaire ;
- stockage securise des mots de passe.

Les mots de passe ne doivent jamais etre stockes en clair.

## Autorisation

Les permissions doivent definir ce qu'un utilisateur peut faire.

Exemples :

- lire les clients ;
- creer une facture ;
- modifier un utilisateur ;
- acceder aux rapports ;
- changer les parametres.

## Secrets

Les secrets ne doivent pas etre commites dans Git.

Exemples :

- cle secrete ;
- mot de passe base de donnees ;
- token ;
- configuration de production.

Utiliser plutot :

- variables d'environnement ;
- fichier `.env.local` ignore par Git ;
- fichier `.env.example` sans valeurs sensibles.

## Validation des donnees

Toutes les donnees qui arrivent dans l'API doivent etre validees avec Pydantic.

## Journalisation

Les actions importantes pourront etre journalisees :

- connexion ;
- creation de donnees sensibles ;
- modification de permissions ;
- suppression ;
- export de rapports.

## Bonnes pratiques

- Ne pas exposer les traces d'erreur techniques aux utilisateurs finaux.
- Ne pas placer de secret dans le code source.
- Tester les routes sensibles.
- Donner le minimum de droits necessaires a chaque role.

