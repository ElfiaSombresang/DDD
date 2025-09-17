
from ecole.domain.entity.cours_entite import CoursEntity
from ecole.domain.entity.eleve_entite import EleveEntity

def test_cours_est_toujours_enseigne_true_when_any_eleve_has_cours():
    c = CoursEntity(id=101, nom="Maths", code="MATH101", professeur_id="P1")
    e1 = EleveEntity(id=1, nom="A", prenom="B", date_naissance="2000-01-01", email="a@b", cours_ids=[101])
    e2 = EleveEntity(id=2, nom="C", prenom="D", date_naissance="2000-01-01", email="c@d", cours_ids=[])
    assert c.cours_est_toujours_enseigne_a_ecole([e1, e2]) is True

def test_cours_est_toujours_enseigne_false_when_no_eleve_has_cours():
    c = CoursEntity(id=999, nom="Astro", code="AST999", professeur_id="P42")
    e1 = EleveEntity(id=1, nom="A", prenom="B", date_naissance="2000-01-01", email="a@b", cours_ids=[101])
    assert c.cours_est_toujours_enseigne_a_ecole([e1]) is False
