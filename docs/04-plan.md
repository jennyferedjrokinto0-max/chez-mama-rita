# 04 — Plan de découpage des tâches

## Tâche 1 : Mise en place de la base de données
- Créer toutes les tables (`users`, `dishes`, `tables`, `orders`, `order_items`).
- *Validation* : Tout est en place et les relations fonctionnent.

## Tâche 2 : Gestion du menu (Pour le gérant)
- Pouvoir ajouter, modifier un plat ou le passer en "épuisé".
- *Validation* : Le gérant gère sa carte facilement.

## Tâche 3 : Prise de commande (Pour le serveur)
- Sélectionner une table, choisir les plats et valider.
- *Validation* : La commande s'enregistre avec le bon statut.

## Tâche 4 : Suivi en cuisine (Pour le cuisinier)
- Voir les commandes entrantes et cliquer pour changer les statuts.
- *Validation* : Le flux de préparation est bien mis à jour en temps réel.

## Tâche 5 : Encaissement (Pour le caissier)
- Calculer l'addition d'une table, encaisser et libérer la table.
- *Validation* : La facture est juste et la table redevient libre.

## Tâche 6 : Tableau de bord (Pour le gérant)
- Afficher le total des ventes de la journée.
- *Validation* : Les chiffres affichés correspondent bien aux encaissements du jour.