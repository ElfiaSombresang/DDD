
import sys
from pathlib import Path
import pytest

# Ensure project root is importable
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

@pytest.fixture
def sample_eleve_dict():
    return {
        "id": 99,
        "nom": "Test",
        "prenom": "User",
        "date_naissance": "2000-01-01",
        "email": "test.user@example.com",
        "cours_ids": [101, 102],
    }
