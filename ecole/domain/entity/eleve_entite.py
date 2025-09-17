from dataclasses import dataclass, field

@dataclass
class EleveEntity:
    id: int
    nom: str
    prenom: str
    date_naissance: str
    email: str
    cours_ids: list = field(default_factory=list)

    def ajouter_cours_a_eleve(self, cours_id: int) -> None:
        self.cours_ids.append(cours_id)

    def retirer_cours_a_eleve(self, cours_id: int) -> None:
        self.cours_ids.remove(cours_id)

    def verifier_si_eleve_a_cours(self, cours_id: int) -> bool:
        return cours_id in self.cours_ids

