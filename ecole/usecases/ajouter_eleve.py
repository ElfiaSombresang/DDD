from injector import inject
from ecole.domain.entity.eleve_entite import EleveEntity
from ecole.domain.repository.eleve_repository_interface import EleveRepositoryInterface

@inject
class AjouterEleve:
    def __init__(self, eleve_repository: EleveRepositoryInterface):
        self.eleve_repository = eleve_repository

    def execute(self, id: int, nom: str, prenom: str, date_naissance: str, email: str, cours_ids: list[int] | None = None) -> EleveEntity:
        eleve = EleveEntity(
            id=id,
            nom=nom,
            prenom=prenom,
            date_naissance=date_naissance,
            email=email,
            cours_ids=cours_ids or []
        )
        return self.eleve_repository.ajouter_ou_mettre_a_jour_eleve(eleve)
