
from ecole.infrastructure.repository.note_repository import NoteRepository
from ecole.domain.entity.note_entite import NoteEntity
from ecole.infrastructure.DB.notes_data import NOTES

def test_ajouter_ou_mettre_a_jour_note_adds_or_updates():
    repo = NoteRepository()
    base_len = len(NOTES)
    n = NoteEntity(id=999, eleve_id=1, cours_id=101, valeur=15.5, coefficient=2.0)
    saved = repo.ajouter_ou_mettre_a_jour_note(n)
    assert saved.id == 999
    assert len(NOTES) == base_len + 1

    # Update same id
    n2 = NoteEntity(id=999, eleve_id=1, cours_id=101, valeur=17.0, coefficient=2.0)
    repo.ajouter_ou_mettre_a_jour_note(n2)
    assert len(NOTES) == base_len + 1
    # Verify the last instance has new value
    assert any(isinstance(x, NoteEntity) and x.id==999 and x.valeur==17.0 for x in NOTES)
