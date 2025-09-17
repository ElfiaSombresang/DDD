from abc import ABC, abstractmethod
from typing import Optional
from ecole.domain.entity.professeur_entite import ProfesseurEntity

class ProfesseurRepositoryInterface(ABC):
    @abstractmethod
    def recuperer_professeur_par_id(self, id: str) -> Optional[ProfesseurEntity]:
        pass
