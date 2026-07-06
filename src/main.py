"""Point d'entrée CLI de Scribe : audio -> transcription -> compte rendu."""

import argparse
import datetime
import sys

from transcription import transcribe
from summary import summarize


def main() -> None:
    parser = argparse.ArgumentParser(description="Scribe : transforme un audio en compte rendu structuré.")
    parser.add_argument("audio_path", help="Chemin du fichier audio à traiter")
    args = parser.parse_args()

    print("Transcription en cours...")
    try:
        transcript = transcribe(args.audio_path)
    except (FileNotFoundError, RuntimeError) as exc:
        sys.exit(f"Erreur : {exc}")

    print("Rédaction du compte rendu en cours...")
    try:
        report = summarize(transcript)
    except RuntimeError as exc:
        sys.exit(f"Erreur : {exc}")

    print("\n" + report)

    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    output_path = f"compte-rendu-{timestamp}.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\nCompte rendu sauvegardé dans {output_path}")


if __name__ == "__main__":
    main()
