from dataclasses import dataclass
from ecole.domain.entity.eleve_entite import EleveEntity

@dataclass
class CoursEntity : 
    id : int
    nom : str
    code : str
    professeur_id : str

    def cours_est_toujours_enseigne_a_ecole(self, eleves : list[EleveEntity]) -> bool : 
        for eleve in eleves : 
            if eleve.verifier_si_eleve_a_cours(self.id) : 
                return True
        return False