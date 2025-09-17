import sys, types
# Provide a lightweight stand-in for the 'injector' package to avoid external dependency during tests
sys.modules.setdefault('injector', types.SimpleNamespace(inject=lambda x: x))


from dataclasses import dataclass
from ecole.domain.entity.eleve_entite import EleveEntity
from ecole.domain.repository.eleve_repository_interface import EleveRepositoryInterface
from ecole.usecases.recuperer_informations_eleve import RecupererInformationEleve
import pytest

@dataclass
class FakeRepo(EleveRepositoryInterface):
    store: dict

    def recuperer_eleve_par_id(self, id: int) -> EleveEntity:
        if id in self.store:
            return self.store[id]
        raise ValueError("not found")

    def ajouter_ou_mettre_a_jour_eleve(self, eleve: EleveEntity) -> EleveEntity:
        self.store[eleve.id] = eleve
        return eleve

def test_recuperer_information_eleve_returns_entity():
    e = EleveEntity(id=42, nom="Nom", prenom="Pre", date_naissance="2000-01-01", email="n@p", cours_ids=[])
    uc = RecupererInformationEleve(eleve_repository=FakeRepo({42: e}))
    out = uc.execute(42)
    assert out == e

def test_recuperer_information_eleve_raises_on_missing():
    uc = RecupererInformationEleve(eleve_repository=FakeRepo({}))
    with pytest.raises(ValueError):
        uc.execute(1)
