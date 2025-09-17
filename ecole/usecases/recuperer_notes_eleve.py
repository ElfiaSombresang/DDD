from injector import inject
from typing import List
from ecole.domain.entity.note_entite import NoteEntity
from ecole.domain.repository.note_repository_interface import NoteRepositoryInterface

@inject
class RecupererNotesEleve:
    def __init__(self, note_repository: NoteRepositoryInterface):
        self.note_repository = note_repository

    def execute(self, eleve_id: int) -> List[NoteEntity]:
        return self.note_repository.lister_notes_par_eleve(eleve_id)
