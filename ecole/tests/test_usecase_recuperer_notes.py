
import sys, types
sys.modules.setdefault('injector', types.SimpleNamespace(inject=lambda x: x))

from ecole.usecases.recuperer_notes_eleve import RecupererNotesEleve
from ecole.domain.repository.note_repository_interface import NoteRepositoryInterface
from ecole.domain.entity.note_entite import NoteEntity
from typing import List

class FakeNotes(NoteRepositoryInterface):
    def __init__(self, data: List[NoteEntity]):
        self.data = data
    def ajouter_ou_mettre_a_jour_note(self, note: NoteEntity) -> NoteEntity:
        self.data.append(note)
        return note
    def lister_notes_par_eleve(self, eleve_id: int) -> List[NoteEntity]:
        return [n for n in self.data if n.eleve_id == eleve_id]

def test_recuperer_notes_returns_filtered():
    notes = [NoteEntity(id=1, eleve_id=7, cours_id=101, valeur=12.0),
             NoteEntity(id=2, eleve_id=7, cours_id=102, valeur=18.0),
             NoteEntity(id=3, eleve_id=8, cours_id=101, valeur=10.0)]
    uc = RecupererNotesEleve(FakeNotes(notes))
    out = uc.execute(7)
    assert len(out) == 2
    assert {n.id for n in out} == {1,2}
