# # # from ecole.domain.entity.eleve_entite import EleveEntity
# # # from ecole.domain.entity.cours_entite import CoursEntity
# # # from ecole.domain.entity.professeur_entite import ProfesseurEntity

# # # def main():

# # #     prof = ProfesseurEntity(id=1, nom="Dupont", prenom="Jean", matière="Maths")

# # #     cours = CoursEntity(id=101, nom="Algèbre", code="MATH101", professeur_id=prof.id)

# # #     eleve = EleveEntity(id=1, nom="Martin", prenom="Alice",
# # #                         date_naissance="2000-05-14",
# # #                         email="alice.martin@mail.fr")


# # #     eleve.ajouter_cours_a_eleve(cours.id)
# # #     print(f"{eleve.prenom} suit les cours : {eleve.cours_ids}")

# # #     print("Alice a le cours de maths ?", eleve.verifier_si_eleve_a_cours(cours.id))

# # #     eleve.retirer_cours_a_eleve(cours.id)
# # #     print(f"Après suppression, {eleve.prenom} suit : {eleve.cours_ids}")

# # #     eleves = [eleve]
# # #     print("Le cours est encore enseigné ?", cours.cours_est_toujours_enseigne_a_ecole(eleves))


# # # if __name__ == "__main__":
# # #     main()



# # from ecole.usecases.recuperer_informations_eleve import RecupererInformationEleve

# # if __name__ == "__main__" : 
# #     usecase = RecupererInformationEleve()
# #     print(usecase.execute(1))


# # main.py
# from dataclasses import asdict, is_dataclass
# import sys

# # 1) Repo concret
# from ecole.infrastructure.repository.eleve_repository import EleveRepository

# # 2) Use case (selon nommage : Information(s))
# try:
#     # ex : class RecupererInformationEleve
#     from ecole.usecases.recuperer_informations_eleve import RecupererInformationEleve as UseCase
# except ImportError:
#     try:
#         # ex : class RecupererInformationsEleve
#         from ecole.usecases.recuperer_informations_eleve import RecupererInformationsEleve as UseCase
#     except ImportError as e:
#         raise ImportError(
#             "Impossible d'importer le use case. Vérifie le nom de la classe dans "
#             "ecole/usecases/recuperer_informations_eleve.py (Information vs Informations)."
#         ) from e

# def pretty_print(obj):
#     if is_dataclass(obj):
#         d = asdict(obj)
#     elif hasattr(obj, "__dict__"):
#         d = obj.__dict__
#     else:
#         d = obj
#     print("\n=== Élève ===")
#     for k, v in d.items():
#         print(f"{k}: {v}")

# def main():
#     # Id élève passé en argument : python main.py 1
#     eleve_id = int(sys.argv[1]) if len(sys.argv) > 1 else 1

#     # Instanciation des dépendances
#     eleve_repository = EleveRepository()
#     usecase = UseCase(eleve_repository)

#     # Appel du use case : certaines versions exposent execute(eleve_id)
#     if hasattr(usecase, "execute"):
#         eleve = usecase.execute(eleve_id)
#     elif hasattr(usecase, "recuperer_eleve_par_id"):
#         eleve = usecase.recuperer_eleve_par_id(eleve_id)
#     else:
#         raise AttributeError(
#             "Le use case ne possède ni 'execute' ni 'recuperer_eleve_par_id'. "
#             "Vérifie la classe dans recuperer_informations_eleve.py."
#         )

#     if eleve is None:
#         print(f"Aucun élève trouvé pour id={eleve_id}")
#     else:
#         pretty_print(eleve)

# if __name__ == "__main__":
#     main()




from kink import di
from ecole.usecases.container import setup_container

from ecole.domain.repository.eleve_repository_interface import EleveRepositoryInterface
from ecole.domain.repository.cours_repository_interface import CoursRepositoryInterface
from ecole.domain.repository.professeur_repository_interface import ProfesseurRepositoryInterface
from ecole.domain.repository.note_repository_interface import NoteRepositoryInterface
from ecole.domain_authentification.repository.utilisateur_repository_interface import UtilisateurRepositoryInterface

from ecole.usecases.ajouter_eleve import AjouterEleve
from ecole.usecases.ajouter_note_eleve import AjouterNoteEleve
from ecole.usecases.recuperer_notes_eleve import RecupererNotesEleve
from ecole.usecases.calculer_obtention_diplome import CalculerObtentionDiplome
from ecole.usecases.lister_cours_professeurs import ListerCoursEtProfesseurs
from ecole.usecases.ajouter_utilisateur import AjouterUtilisateur



def main():
    setup_container()

    eleve_repo = di[EleveRepositoryInterface]
    cours_repo = di[CoursRepositoryInterface]
    prof_repo = di[ProfesseurRepositoryInterface]
    note_repo = di[NoteRepositoryInterface]
    utilisateur_repo = di[UtilisateurRepositoryInterface]


    ajouter_eleve = AjouterEleve(eleve_repo)
    ajouter_note = AjouterNoteEleve(note_repo, eleve_repo, cours_repo)
    recuperer_notes = RecupererNotesEleve(note_repo)
    calcul_diplome_obtenu = CalculerObtentionDiplome(note_repo)
    liste_cours_professeur = ListerCoursEtProfesseurs(cours_repo, prof_repo)
    ajouter_utilisateur = AjouterUtilisateur(utilisateur_repo)



    # id_eleve = int(input("Entrez l'identifiant de l'élève : \n"))
    # notes = recuperer_notes.execute(id_eleve)
    # print("Notes:", notes)
    # resultat = calcul_diplome_obtenu.execute(id_eleve)
    # print("Diplôme obtenu:", resultat, "| moyenne:", calcul_diplome_obtenu.derniere_moyenne)


    # eleve = ajouter_eleve.execute(
    #     id = int(input("Entrez l'id de l'élève à inscrire : \n")), 
    #     nom = input("Entrez le nom de l'élève à inscrire : \n"), 
    #     prenom = input("Entrez le prénom de l'élève à inscrire : \n"),
    #     date_naissance = input("Entrez la date de naissance de l'élève à inscrire (format jj-mm-aaaa) : \n"), 
    #     email = input("Entrez l'email de l'élève à inscrire : \n"),
    #     cours_ids=[c.strip() for c in (input("Entrez la liste de cours auxquels l'élève est inscrit (les ids séparées par des ',') : \n")).split(",") if c.strip()]
    # )
    # print(eleve)

    # ajouter_note.execute(id=1, eleve_id=id_eleve, cours_id=101, valeur=12.0, coefficient=2.0)
    # ajouter_note.execute(id=2, eleve_id=id_eleve, cours_id=102, valeur=8.0,  coefficient=1.0)

    # notes = recuperer_notes.execute(id_eleve)
    # print("Notes:", notes)

    # resultat = calcul_diplome_obtenu.execute(id_eleve)
    # print("Diplôme obtenu:", resultat, "| moyenne:", calcul_diplome_obtenu.derniere_moyenne)

    # for row in liste_cours_professeur.execute():
    #     print(row)

    utilisateur = ajouter_utilisateur.execute(
        id = int(input("Entrez l'id de l'utilisateur à créer : \n")), 
        nom = input("Entrez le nom de l'utilisateur à créer : \n"), 
        prenom = input("Entrez le prénom de l'utilisateur à créer : \n"),
        statut = input("Entrez le statut de l'utilisateur à créer (professeur, étudiant ou personnel administratif) : \n"), 
        email = input("Entrez l'email de l'utilisateur à créer : \n"),
    )
    print(utilisateur)


if __name__ == "__main__":
    main()