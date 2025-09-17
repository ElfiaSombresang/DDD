from kink import di

from ecole.domain.repository.eleve_repository_interface import EleveRepositoryInterface
from ecole.infrastructure.repository.eleve_repository import EleveRepository
from ecole.domain.repository.cours_repository_interface import CoursRepositoryInterface
from ecole.infrastructure.repository.cours_repository import CoursRepository
from ecole.domain.repository.professeur_repository_interface import ProfesseurRepositoryInterface
from ecole.infrastructure.repository.professeur_repository import ProfesseurRepository
from ecole.domain.repository.note_repository_interface import NoteRepositoryInterface
from ecole.infrastructure.repository.note_repository import NoteRepository
from ecole.domain_authentification.repository.utilisateur_repository_interface import UtilisateurRepositoryInterface
from ecole.infrastructure.repository.utilisateur_repository import UtilisateurRepository

def setup_container():
    di[EleveRepositoryInterface] = EleveRepository()
    di[CoursRepositoryInterface] = CoursRepository()
    di[ProfesseurRepositoryInterface] = ProfesseurRepository()
    di[NoteRepositoryInterface] = NoteRepository()
    di[UtilisateurRepositoryInterface] = UtilisateurRepository()
