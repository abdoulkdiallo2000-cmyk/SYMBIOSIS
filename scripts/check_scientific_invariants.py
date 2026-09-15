"""Cross-document acceptance checks for the current SYMBIOSIS-Zero invariants."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = {
    "protocol": ROOT / "docs/SYMBIOSIS-ZERO-EXPERIMENTAL-PROTOCOL-v1.0.md",
    "battery": ROOT / "docs/SYMBIOSIS-ZERO-TASK-BATTERY-v1.0.md",
    "summary": ROOT / "docs/SYMBIOSIS-ZERO.md",
    "dictionary": ROOT / "docs/DATA-DICTIONARY.md",
    "stop": ROOT / "docs/SYMBIOSIS-Zero-STOP-H7-Questionnaire.md",
    "h9": ROOT / "docs/SYMBIOSIS-Zero-H9-Transparency-Template.md",
    "fr": ROOT / "docs/white-paper/SYMBIOSIS-WHITE-PAPER-v1.0-FR.md",
    "en": ROOT / "docs/white-paper/SYMBIOSIS-WHITE-PAPER-v1.0-EN.md",
}


def require(text: str, *fragments: str) -> None:
    for fragment in fragments:
        assert fragment in text, fragment


def main() -> None:
    text = {name: path.read_text(encoding="utf-8") for name, path in DOCS.items()}
    for name in ("protocol", "battery", "summary", "fr", "en"):
        require(text[name], "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9")
    for name in ("protocol", "summary", "fr", "en"):
        require(text[name], "PRE", "H+AI", "SZ", "AI", "POST")
    require(text["protocol"], "paramétriques", "H6 et H8", "portes H7/H9")
    require(text["battery"], "H6 et H8 restent exploratoires", "H7 et H9 sont des portes")
    require(text["stop"], "REFUSER", "PAUSE", "STOP")
    require(text["h9"], "indépendamment de la performance")
    require(text["fr"], "mesures non invasives seulement optionnelles", "Aucune somme pondérée")
    require(text["en"], "non-invasive measurements only as optional", "No weighted sum")

    public_files = [ROOT / "README.md", ROOT / "ROADMAP.md", ROOT / "docs/PRINCIPLES.md",
                    ROOT / "docs/ARCHITECTURE.md", ROOT / "docs/SYMBIOSIS-ZERO.md",
                    DOCS["battery"], DOCS["stop"], DOCS["h9"], DOCS["fr"], DOCS["en"]]
    public = "\n".join(p.read_text(encoding="utf-8") for p in public_files).lower()
    forbidden = ["batterie v0.1", "without compensating benefit", "neurotechnology and neurorights",
                 "l'émotion a toujours raison", "the emotion is always right"]
    for phrase in forbidden:
        assert phrase not in public, phrase
    print("PASS: scientific status, conditions, STOP, gates, optional instrumentation and forbidden-formulation checks passed.")


if __name__ == "__main__":
    main()
