from dataclasses import dataclass

@dataclass
class ProfesseurEntity : 
    id : int
    nom : str
    prenom : str
    matière : str