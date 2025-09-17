from dataclasses import dataclass, field

@dataclass
class UtilisateurEntite:
    id: int
    nom: str
    prenom: str
    statut: str # professeur, etudiant, personnel administratif
    email: str