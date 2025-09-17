from injector import inject
from typing import List, Dict, Any
from ecole.domain.repository.cours_repository_interface import CoursRepositoryInterface
from ecole.domain.repository.professeur_repository_interface import ProfesseurRepositoryInterface

@inject
class ListerCoursEtProfesseurs:
    def __init__(self, cours_repository: CoursRepositoryInterface, professeur_repository: ProfesseurRepositoryInterface):
        self.cours_repository = cours_repository
        self.professeur_repository = professeur_repository

    def execute(self) -> List[Dict[str, Any]]:
        result: List[Dict[str, Any]] = []
        for cours in self.cours_repository.lister_tous_les_cours():
            prof = self.professeur_repository.recuperer_professeur_par_id(str(cours.professeur_id))
            nom_prof = f"{prof.prenom} {prof.nom}" if prof else "Inconnu"
            result.append({
                "cours_id": cours.id,
                "cours_nom": cours.nom,
                "cours_code": cours.code,
                "professeur_id": cours.professeur_id,
                "professeur_nom_complet": nom_prof
            })
        return result
