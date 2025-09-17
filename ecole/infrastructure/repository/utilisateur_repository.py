from dataclasses import asdict

from ecole.domain_authentification.repository.utilisateur_repository_interface import UtilisateurRepositoryInterface
from ecole.domain_authentification.entity.utilisateur_entite import UtilisateurEntite
from ecole.infrastructure.DB.utilisateurs_data import UTILISATEURS

class UtilisateurRepository(UtilisateurRepositoryInterface) : 


    def ajouter_ou_mettre_a_jour_utilisateur(self, utilisateur: UtilisateurEntite) -> UtilisateurEntite:

        for i, u in enumerate(UTILISATEURS):
            if isinstance(u, UtilisateurEntite) and u.id == utilisateur.id:
                UTILISATEURS[i] = utilisateur
                return utilisateur
            if isinstance(u, dict) and u.get("id") == utilisateur.id:
                UTILISATEURS[i] = utilisateur
                return utilisateur
        UTILISATEURS.append(utilisateur)
        return utilisateur
