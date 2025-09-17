from injector import inject
from ecole.domain.repository.eleve_repository_interface import EleveRepositoryInterface
from ecole.domain.entity.eleve_entite import EleveEntity

@inject
class RecupererInformationEleve:
    def __init__(self, eleve_repository: EleveRepositoryInterface):
        self.eleve_repository = eleve_repository

    def execute(self, eleve_id: int) -> EleveEntity | None:
        return self.eleve_repository.recuperer_eleve_par_id(eleve_id)
    
    def recuperer_eleve_par_id(self, eleve_id: int) -> EleveEntity | None:
        return self.eleve_repository.recuperer_eleve_par_id(eleve_id)
