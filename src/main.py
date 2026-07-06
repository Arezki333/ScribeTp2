"""Point d'entrée CLI de Scribe : audio -> transcription -> compte rendu."""

import argparse
import datetime
import os
import sys

from transcription import transcribe
from moderation import is_legitimate
from summary import summarize

TRANSCRIPTIONS_DIR = "transcriptions"


def main() -> None:
    parser = argparse.ArgumentParser(description="Scribe : transforme un audio en compte rendu structuré.")
    parser.add_argument("audio_path", help="Chemin du fichier audio à traiter")
    args = parser.parse_args()

    print("Transcription en cours...")
    try:
        transcript = transcribe(args.audio_path)
    except (FileNotFoundError, RuntimeError) as exc:
        sys.exit(f"Erreur : {exc}")

    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    print("Vérification du contenu...")
    try:
        if not is_legitimate(transcript):
            sys.exit(
                "Scribe ne peut pas traiter cet enregistrement : son contenu "
                "semble chercher à détourner l'outil de son usage prévu."
            )
    except RuntimeError as exc:
        sys.exit(f"Erreur : {exc}")

    print("Rédaction du compte rendu en cours...")
    try:
        report = summarize(transcript)
    except RuntimeError as exc:
        sys.exit(f"Erreur : {exc}")

    print("\n" + report)

    os.makedirs(TRANSCRIPTIONS_DIR, exist_ok=True)
    output_path = os.path.join(TRANSCRIPTIONS_DIR, f"compte-rendu-{timestamp}.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\nCompte rendu sauvegardé dans {output_path}")


if __name__ == "__main__":
    main()
