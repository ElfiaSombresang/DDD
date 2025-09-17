import pytest
from dataclasses import asdict
from ecole.domain.entity.eleve_entite import EleveEntity

class TestEntiteEleve:
    @pytest.fixture(autouse=True)
    def _setup(self):
        self.bonne_entite = {
            "id": 3,
            "nom": "Bernard",
            "prenom": "Sophie",
            "date_naissance": "2001-03-08",
            "email": "sophie.bernard@example.com",
            "cours_ids": [101, 105],
        }

    def test_creation_entite_et_clefs(self):
        # given
        bonne_entite = self.bonne_entite
        # when
        eleve = EleveEntity(**bonne_entite)
        clefs_entite = list(asdict(eleve).keys())
        clefs_attendues = ["id", "nom", "prenom", "date_naissance", "email", "cours_ids"]
        # then
        assert isinstance(eleve, EleveEntity)
        assert clefs_entite == clefs_attendues
        assert isinstance(bonne_entite["cours_ids"], list)

    def test_ajouter_cours(self):
        eleve = EleveEntity(**self.bonne_entite)
        eleve.ajouter_cours_a_eleve(999)
        assert 999 in eleve.cours_ids

    def test_retirer_cours(self):
        eleve = EleveEntity(**self.bonne_entite)
        eleve.ajouter_cours_a_eleve(999)
        eleve.retirer_cours_a_eleve(999)
        assert 999 not in eleve.cours_ids

    def test_verifier_si_eleve_a_cours(self):
        eleve = EleveEntity(**self.bonne_entite)
        assert eleve.verifier_si_eleve_a_cours(101) is True
        assert eleve.verifier_si_eleve_a_cours(999) is False