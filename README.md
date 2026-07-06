# Scribe

Scribe est un outil en ligne de commande qui transforme un enregistrement audio (réunion, cours, note vocale) en compte rendu écrit et structuré.

Le traitement se déroule en deux étapes, appuyées sur l'API serverless de [Groq](https://console.groq.com/docs/overview) :

1. **Transcription** : un modèle Speech-to-Text convertit l'audio en texte brut.
2. **Compte rendu** : un LLM reformule ce texte en un compte rendu structuré (titre, résumé, points clés, décisions/actions).

## Installation

```bash
git clone https://github.com/Arezki333/ScribeTp2.git
cd ScribeTp2
python -m venv venv
source venv/bin/activate  # Windows : venv\Scripts\activate
pip install -r requirements.txt
```

Une clé API Groq est nécessaire (voir [console.groq.com](https://console.groq.com)). Elle se configure via un fichier `.env` (détails à venir à l'étape *Configuration*).

## Utilisation

```bash
python src/main.py chemin/vers/audio.mp3
```

*(à compléter au fil du TP)*

## Structure du projet

```
ScribeTp2/
├── src/            # code source de l'application
├── audio/samples/  # exemples d'enregistrements audio pour les tests/démos
├── requirements.txt
├── .env.example
└── README.md
```

- `src/` regroupe le code Python de l'application, séparé de la configuration du dépôt à la racine.
- `audio/samples/` contient des exemples d'audio courts servant à tester la transcription, distincts du code.

## Choix des modèles

*(à compléter à l'étape Configuration — Q2)*

## Réponses aux questions

### Q1 — Pourquoi le `.gitignore` doit exister avant d'écrire la moindre ligne de code manipulant des secrets ?

Parce que Git suit l'historique, pas seulement l'état courant : dès qu'un fichier contenant une clé (par exemple `.env`) est commité une seule fois, cette clé reste consultable dans l'historique même si le fichier est supprimé ou modifié ensuite (`git log`, `git show`, clone du dépôt...). La retirer après coup demande de réécrire l'historique (`git filter-repo`, `BFG`...), ce qui est lourd, risqué sur un dépôt déjà partagé, et n'empêche pas qu'elle ait déjà pu être exposée (dépôt public, fork, clone local d'un collaborateur). Mettre en place le `.gitignore` avant d'introduire `.env` évite structurellement qu'un `git add` ou un `git add -A` n'inclue le secret par erreur : la protection est en place avant que le risque n'existe.
