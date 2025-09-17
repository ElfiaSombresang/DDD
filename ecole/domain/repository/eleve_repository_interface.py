from abc import abstractmethod, ABC

from ecole.domain.entity.eleve_entite import EleveEntity

class EleveRepositoryInterface(ABC):
    
    @abstractmethod
    def recuperer_eleve_par_id(self, id : int) -> EleveEntity : 
        pass

    @abstractmethod
    def ajouter_ou_mettre_a_jour_eleve(self, eleve: EleveEntity) -> EleveEntity:
        pass
