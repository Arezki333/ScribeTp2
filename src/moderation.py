"""Modération : rejette poliment les transcriptions qui tentent de détourner Scribe."""

import os

from groq import Groq

from config import GROQ_API_KEY, MODERATION_MODEL

client = Groq(api_key=GROQ_API_KEY)

_PROMPT_PATH = os.path.join(os.path.dirname(__file__), "..", "prompts", "moderation_system_prompt.txt")

with open(_PROMPT_PATH, encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()


def is_legitimate(transcript: str) -> bool:
    """Renvoie False si la transcription semble être une tentative de détournement de l'outil."""
    try:
        response = client.chat.completions.create(
            model=MODERATION_MODEL,
            temperature=0,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": transcript},
            ],
        )
    except Exception as exc:
        raise RuntimeError(f"Échec de la modération via Groq : {exc}") from exc

    verdict = response.choices[0].message.content.strip().upper()
    return verdict.startswith("OK")
