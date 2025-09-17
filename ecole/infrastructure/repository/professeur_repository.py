from typing import Optional
from ecole.domain.repository.professeur_repository_interface import ProfesseurRepositoryInterface
from ecole.domain.entity.professeur_entite import ProfesseurEntity
from ecole.infrastructure.DB.professeurs_data import PROFESSEURS

class ProfesseurRepository(ProfesseurRepositoryInterface):
    def recuperer_professeur_par_id(self, id: str) -> Optional[ProfesseurEntity]:
        for p in PROFESSEURS:
            if isinstance(p, ProfesseurEntity) and str(p.id) == str(id):
                return p
            if isinstance(p, dict) and str(p.get("id")) == str(id):
                return ProfesseurEntity(**p)
        return None
