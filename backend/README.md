# Backend — SmartMeeting Summarizer

Ce dossier contient le backend du projet SmartMeeting Summarizer

Le backend est une **API REST construite avec FastAPI**, responsable de :
- la réception des fichiers
- la transcription audio
- l’analyse NLP
- la génération des résultats structurés

---

## Prérequis

- Python 3.9 ou supérieur
- pip
- Environnement virtuel recommandé

---

## Création de l’environnement virtuel

### Créer l’environnement virtuel

```bash
python -m venv venv

```

Pour activer :

Sur Windows

```bash
venv\Scripts\activate

```

Sur Mac

```bash
source venv/bin/activate

```

Installation des dépendances

```bash

pip install -r requirements.txt

```
