def test_creation_commande_table():
    commande = {
        "table_id": 4,
        "serveur_id": 1,
        "items": [{"dish_id": 2, "quantite": 2}],
        "statut": "recue"
    }
    assert commande["table_id"] == 4
    assert commande["statut"] == "recue"
    assert len(commande["items"]) > 0