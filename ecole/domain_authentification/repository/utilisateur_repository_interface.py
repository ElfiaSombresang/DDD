from abc import abstractmethod, ABC

from ecole.domain_authentification.entity.utilisateur_entite import UtilisateurEntite

class UtilisateurRepositoryInterface(ABC):

    @abstractmethod
    def ajouter_ou_mettre_a_jour_utilisateur(self, eleve: UtilisateurEntite) -> UtilisateurEntite:
        pass
