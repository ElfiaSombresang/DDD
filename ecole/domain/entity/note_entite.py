from dataclasses import dataclass

@dataclass
class NoteEntity:
    id: int
    eleve_id: int
    cours_id: int
    valeur: float          
    coefficient: float = 1.0