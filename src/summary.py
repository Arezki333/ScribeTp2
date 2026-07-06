"""Génération d'un compte rendu structuré à partir d'une transcription brute, via Groq."""

import os

from groq import Groq

from config import GROQ_API_KEY, LLM_MODEL

client = Groq(api_key=GROQ_API_KEY)

_PROMPT_PATH = os.path.join(os.path.dirname(__file__), "..", "prompts", "summary_system_prompt.txt")

with open(_PROMPT_PATH, encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()


def summarize(transcript: str) -> str:
    """Transforme une transcription brute en compte rendu structuré (Markdown)."""
    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            temperature=0.2,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": transcript},
            ],
        )
    except Exception as exc:
        raise RuntimeError(f"Échec de la génération du compte rendu via Groq : {exc}") from exc

    return response.choices[0].message.content
