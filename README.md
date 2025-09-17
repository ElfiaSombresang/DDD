# Projet : Développement Orienté Objet - Gestion d'une École

## Objectif
Ce projet est une application Python qui illustre les principes de **programmation orientée objet** et de **Clean Architecture (DDD / Domain-Driven Design)**.  
Il permet de gérer les entités d'une école : **élèves, cours, professeurs et notes** à travers une structure modulaire.

---

## Structure du projet
```
Dev_oriente_objet/
│── main.py                 # Point d'entrée principal
│── requirements.txt        # Dépendances Python
│── README.md               # Documentation
│
├── ecole/
│   ├── domain/             # Couches métier
│   │   ├── entity/         # Entités (Eleve, Professeur, Cours, Note)
│   │   └── repository/     # Interfaces des repositories
│   │
│   ├── infrastructure/     # Implémentations concrètes (ex: mémoire)
│   └── usecases/           # Cas d'utilisation (ajouter élève, récupérer infos, etc.)
│
└── .venv/                  # Environnement virtuel (non inclus dans le dépôt Git)
```

---

## Installation
### 1. Cloner le projet
```bash
git clone https://github.com/votrecompte/projet_ecole.git
cd projet_ecole/Dev_oriente_objet
```

### 2. Créer un environnement virtuel
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

---

## Exécution
Lancer le projet :
```bash
python main.py
```

---

## Exemple d'utilisation
- Ajouter un élève  
- Récupérer ses informations  
- Vérifier ses cours  
- Associer des notes  

Le fichier `main.py` contient des **scénarios de test** pour démontrer les fonctionnalités.

---

## Architecture
- **Entities** : représentent les objets métier (Élève, Cours, Professeur, Note).  
- **Repository Interfaces** : définissent les contrats d’accès aux données.  
- **Use Cases** : implémentent la logique métier (ajouter un élève, récupérer un élève par ID, etc.).  
- **Infrastructure** : implémente les repositories (exemple en mémoire).  

