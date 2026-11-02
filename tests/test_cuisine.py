def test_changement_statut_cuisine():
    statuts = ["recue", "en_preparation", "prete"]
    actuel = statuts[0]
    
    actuel = statuts[1]
    assert actuel == "en_preparation"
    
    actuel = statuts[2]
    assert actuel == "prete"