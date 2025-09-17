
import pytest
from ecole.infrastructure.repository.eleve_repository import EleveRepository
from ecole.domain.entity.eleve_entite import EleveEntity
from ecole.infrastructure.DB.eleves_data import ELEVES

def test_recuperer_eleve_par_id_returns_entity():
    repo = EleveRepository()
    # pick an existing id from dummy data (1 should exist)
    eleve = repo.recuperer_eleve_par_id(1)
    assert isinstance(eleve, EleveEntity)
    assert eleve.id == 1

def test_recuperer_eleve_par_id_raises_for_unknown():
    repo = EleveRepository()
    with pytest.raises(ValueError):
        repo.recuperer_eleve_par_id(99999)

def test_ajouter_ou_mettre_a_jour_eleve_replaces_when_same_id():
    repo = EleveRepository()
    original_len = len(ELEVES)
    e = EleveEntity(id=1, nom="X", prenom="Y", date_naissance="1990-01-01", email="x@y", cours_ids=[])
    saved = repo.ajouter_ou_mettre_a_jour_eleve(e)
    assert saved.id == 1
    # length should not increase when replacing
    assert len(ELEVES) == original_len
