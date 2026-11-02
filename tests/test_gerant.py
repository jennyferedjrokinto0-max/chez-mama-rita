def test_calcul_ventes_du_jour():
    ventes = [
        {"total": 9000, "statut": "payee"},
        {"total": 4500, "statut": "payee"}
    ]
    total_ventes = sum(v["total"] for v in ventes if v["statut"] == "payee")
    assert total_ventes == 13500