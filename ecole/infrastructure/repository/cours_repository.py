from typing import List, Optional
from ecole.domain.repository.cours_repository_interface import CoursRepositoryInterface
from ecole.domain.entity.cours_entite import CoursEntity
from ecole.infrastructure.DB.cours_data import COURS

class CoursRepository(CoursRepositoryInterface):
    def lister_tous_les_cours(self) -> List[CoursEntity]:
        out = []
        for c in COURS:
            if isinstance(c, CoursEntity):
                out.append(c)
            elif isinstance(c, dict):
                out.append(CoursEntity(**c))
        return out

    def recuperer_cours_par_id(self, id: int) -> Optional[CoursEntity]:
        for c in COURS:
            if isinstance(c, CoursEntity) and c.id == id:
                return c
            if isinstance(c, dict) and c.get("id") == id:
                return CoursEntity(**c)
        return None
