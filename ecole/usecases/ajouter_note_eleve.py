from injector import inject
from ecole.domain.entity.note_entite import NoteEntity
from ecole.domain.repository.note_repository_interface import NoteRepositoryInterface
from ecole.domain.repository.eleve_repository_interface import EleveRepositoryInterface
from ecole.domain.repository.cours_repository_interface import CoursRepositoryInterface

@inject
class AjouterNoteEleve:
    def __init__(self, note_repository: NoteRepositoryInterface,
                 eleve_repository: EleveRepositoryInterface,
                 cours_repository: CoursRepositoryInterface):
        self.note_repository = note_repository
        self.eleve_repository = eleve_repository
        self.cours_repository = cours_repository

    def execute(self, id: int, eleve_id: int, cours_id: int, valeur: float, coefficient: float = 1.0) -> NoteEntity:
        if not (0.0 <= valeur <= 20.0):
            raise ValueError("La note doit être comprise entre 0 et 20.")
        if self.eleve_repository.recuperer_eleve_par_id(eleve_id) is None:
            raise ValueError("Élève introuvable.")
        if self.cours_repository.recuperer_cours_par_id(cours_id) is None:
            raise ValueError("Cours introuvable.")
        note = NoteEntity(id=id, eleve_id=eleve_id, cours_id=cours_id, valeur=valeur, coefficient=coefficient)
        return self.note_repository.ajouter_ou_mettre_a_jour_note(note)
