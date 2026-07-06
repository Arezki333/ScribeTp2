"""Configuration centralisée de Scribe : clé API et identifiants des modèles Groq."""

import os
import sys

from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    sys.exit(
        "Erreur : la variable d'environnement GROQ_API_KEY est manquante.\n"
        "Copiez .env.example vers .env et renseignez votre clé API Groq "
        "(https://console.groq.com/keys)."
    )

# Seul endroit du projet où les noms de modèles sont définis.
STT_MODEL = "whisper-large-v3-turbo"
LLM_MODEL = "llama-3.3-70b-versatile"
MODERATION_MODEL = "llama-3.1-8b-instant"
