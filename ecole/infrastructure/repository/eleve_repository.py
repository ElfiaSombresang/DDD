from dataclasses import asdict

from ecole.domain.repository.eleve_repository_interface import EleveRepositoryInterface
from ecole.domain.entity.eleve_entite import EleveEntity
from ecole.infrastructure.DB.eleves_data import ELEVES

class EleveRepository(EleveRepositoryInterface) : 

    def recuperer_eleve_par_id(self, id : int) -> dict :
 
        for e in ELEVES:
            if isinstance(e, EleveEntity) and e.id == id:
                return e
            if isinstance(e, dict) and e.get("id") == id:
                return EleveEntity(**e)
        raise ValueError(f"Élève introuvable pour id={id}")

        # liste_eleves = self._serialiser_fichier_json("ecole/infrastructure/db/eleves.json")
        # eleve_parametre = list(filter(lambda x : x["id"]==2, liste_eleves))[0]
        # eleve = EleveEntity(**eleve_parametre)
        # return asdict(eleve)

        # @staticmethod

        # def _serialiser_fichier_json(file_path : str) -> list :
        #     with open(file_path) as file : 
        #         data = json.load(file)
        #     return data


    def ajouter_ou_mettre_a_jour_eleve(self, eleve: EleveEntity) -> EleveEntity:

        for i, e in enumerate(ELEVES):
            if isinstance(e, EleveEntity) and e.id == eleve.id:
                ELEVES[i] = eleve
                return eleve
            if isinstance(e, dict) and e.get("id") == eleve.id:
                ELEVES[i] = eleve
                return eleve
        ELEVES.append(eleve)
        return eleve
