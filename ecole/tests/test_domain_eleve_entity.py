
from dataclasses import asdict
from ecole.domain.entity.eleve_entite import EleveEntity

def test_eleve_entity_init(sample_eleve_dict):
    eleve = EleveEntity(**sample_eleve_dict)
    assert isinstance(eleve, EleveEntity)
    assert asdict(eleve) == sample_eleve_dict

def test_ajouter_cours_a_eleve_appends_id(sample_eleve_dict):
    eleve = EleveEntity(**sample_eleve_dict)
    eleve.ajouter_cours_a_eleve(103)
    assert 103 in eleve.cours_ids
