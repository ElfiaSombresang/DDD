# Projet École - Architecture DDD (Domain Driven Design)

Ce projet est une implémentation en Python d'une gestion d'école suivant l'architecture **Domain Driven Design (DDD)**.  
Il permet de gérer les élèves, les cours, les professeurs et les notes, avec séparation claire entre **domain**, **usecases** et **infrastructure**.

---

## 🚀 Prérequis

- Python 3.10 ou plus
- `pip` pour installer les dépendances
- Virtualenv recommandé

---

## 📦 Installation

1. Cloner le dépôt :
   ```bash
   git clone <url-du-repo>
   cd Dev_oriente_objet
   ```

2. Créer un environnement virtuel :
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate    # Windows
   ```

3. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

---

## 🏗️ Structure du projet

```
Dev_oriente_objet/
│── ecole/
│   ├── domain/          # Entités, interfaces, règles métier
│   │   ├── entity/
│   │   ├── repository/
│   │   └── service/
│   │
│   ├── usecases/        # Cas d’usage (logique applicative)
│   │   ├── ajouter_eleve.py
│   │   ├── recuperer_information_eleve.py
│   │   └── ...
│   │
│   ├── infrastructure/  # Implémentations concrètes des dépôts
│   │   └── eleve_repository.py
│   │
│   └── __init__.py
│
│── tests/               # Tests unitaires et d’intégration
│── main.py              # Point d’entrée principal
│── requirements.txt     # Dépendances Python
│── README.md            # Documentation du projet
```

---

## ▶️ Exécution

Lancer le programme principal :

```bash
python main.py
```

Celui-ci permet d’ajouter des élèves, de les inscrire à des cours et de récupérer leurs informations.

---

## 🧪 Tests

Les tests sont disponibles dans le dossier `tests/`.

Exécuter tous les tests :

```bash
pytest tests/
```

---

## 📖 Notes

- Le projet suit une architecture **DDD** pour séparer la logique métier (domain), les cas d’usage (usecases) et l’infrastructure.
- Les données sont stockées en mémoire dans des listes Python pour l’instant (implémentation simplifiée).

---

## ✨ Auteurs

- Projet réalisé dans le cadre du cours de **Développement Orienté Objet (M1)**  
- Auteur : *Priscillia Marques Rodrigues*
