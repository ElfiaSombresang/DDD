from injector import inject
from ecole.domain_authentification.entity.utilisateur_entite import UtilisateurEntite
from ecole.domain_authentification.repository.utilisateur_repository_interface import UtilisateurRepositoryInterface

@inject
class AjouterUtilisateur:
    def __init__(self, eleve_repository: UtilisateurRepositoryInterface):
        self.eleve_repository = eleve_repository

    def execute(self, id: int, nom: str, prenom: str, statut: str, email: str) -> UtilisateurEntite:
        utilisateur = UtilisateurEntite(
            id = id,
            nom = nom,
            prenom = prenom,
            statut= statut, # professeur, etudiant, personnel administratif
            email = email
        )
        return self.eleve_repository.ajouter_ou_mettre_a_jour_utilisateur(utilisateur)
