"""Transcription audio via le modèle Speech-to-Text de Groq."""

import os

from groq import Groq

from config import GROQ_API_KEY, STT_MODEL

client = Groq(api_key=GROQ_API_KEY)


def transcribe(audio_path: str) -> str:
    """Transcrit un fichier audio en texte brut via l'API Groq.

    Lève FileNotFoundError si le fichier n'existe pas, RuntimeError si
    l'API renvoie une erreur.
    """
    if not os.path.isfile(audio_path):
        raise FileNotFoundError(f"Fichier audio introuvable : {audio_path}")

    with open(audio_path, "rb") as audio_file:
        try:
            response = client.audio.transcriptions.create(
                file=audio_file,
                model=STT_MODEL,
            )
        except Exception as exc:
            raise RuntimeError(f"Échec de la transcription via Groq : {exc}") from exc

    return response.text
