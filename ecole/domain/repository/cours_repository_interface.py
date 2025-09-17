from abc import ABC, abstractmethod
from typing import List, Optional
from ecole.domain.entity.cours_entite import CoursEntity

class CoursRepositoryInterface(ABC):
    @abstractmethod
    def lister_tous_les_cours(self) -> List[CoursEntity]:
        pass

    @abstractmethod
    def recuperer_cours_par_id(self, id: int) -> Optional[CoursEntity]:
        pass
