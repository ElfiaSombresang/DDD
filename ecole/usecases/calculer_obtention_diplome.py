from injector import inject
from ecole.domain.repository.note_repository_interface import NoteRepositoryInterface

@inject
class CalculerObtentionDiplome:
    def __init__(self, note_repository: NoteRepositoryInterface):
        self.note_repository = note_repository
        self.derniere_moyenne: float | None = None

    def execute(self, eleve_id: int) -> bool:
        notes = self.note_repository.lister_notes_par_eleve(eleve_id)
        if not notes:
            self.derniere_moyenne = None
            return False

        total = sum(n.valeur * n.coefficient for n in notes)
        coef = sum(n.coefficient for n in notes) or 1.0
        self.derniere_moyenne = total / coef


        if any(n.valeur < 6 for n in notes):
            return False
        return self.derniere_moyenne >= 10.0
