from typing import List
from ecole.domain.repository.note_repository_interface import NoteRepositoryInterface
from ecole.domain.entity.note_entite import NoteEntity
from ecole.infrastructure.DB.notes_data import NOTES

class NoteRepository(NoteRepositoryInterface):
    def ajouter_ou_mettre_a_jour_note(self, note: NoteEntity) -> NoteEntity:
        
        found = None
        for i, n in enumerate(NOTES):
            if isinstance(n, NoteEntity) and n.id == note.id:
                NOTES[i] = note
                found = note
                break
            if isinstance(n, dict) and n.get("id") == note.id:
                NOTES[i] = note
                found = note
                break
        if not found:
            NOTES.append(note)
        return note

    def lister_notes_par_eleve(self, eleve_id: int) -> List[NoteEntity]:
        out = []
        for n in NOTES:
            if isinstance(n, NoteEntity) and n.eleve_id == eleve_id:
                out.append(n)
            elif isinstance(n, dict) and n.get("eleve_id") == eleve_id:
                out.append(NoteEntity(**n))
        return out
