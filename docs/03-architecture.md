## La stack qu'on retient
- **Côté technique** : Un backend simple et efficace (PHP/Laravel ou Python), avec une interface propre en HTML/Tailwind CSS pour que ce soit fluide sur n'importe quel écran.
- **Base de données** : SQLite ou PostgreSQL pour stocker proprement les tables, les plats et les commandes.

## Les tables principales
1. **`users`** : Les comptes et les rôles (serveur, cuisinier, caissier, gérant).
2. **`dishes`** : Les plats, leurs prix et si c'est dispo ou non.
3. **`tables`** : Les tables du resto et leur statut (libre, occupée).
4. **`orders`** : Les commandes en cours rattachées à une table.
5. **`order_items`** : Le détail de ce qu'il y a dans chaque commande.