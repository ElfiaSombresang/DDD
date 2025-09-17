from abc import ABC, abstractmethod
from typing import List, Iterable
from ecole.domain.entity.note_entite import NoteEntity

class NoteRepositoryInterface(ABC):
    @abstractmethod
    def ajouter_ou_mettre_a_jour_note(self, note: NoteEntity) -> NoteEntity:
        pass

    @abstractmethod
    def lister_notes_par_eleve(self, eleve_id: int) -> List[NoteEntity]:
        pass
