def test_calcul_total_facture():
    items = [
        {"nom": "Poisson Frit", "prix": 3000, "quantite": 2},
        {"nom": "Boisson", "prix": 1000, "quantite": 3}
    ]
    total = sum(i["prix"] * i["quantite"] for i in items)
    assert total == 9000