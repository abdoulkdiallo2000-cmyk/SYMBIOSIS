"""Check the verified White Paper bibliography and FR/EN identity."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FR = ROOT / "docs/white-paper/SYMBIOSIS-WHITE-PAPER-v1.0-FR.md"
EN = ROOT / "docs/white-paper/SYMBIOSIS-WHITE-PAPER-v1.0-EN.md"

EXPECTED = {
    "10.1145/3449287": ("Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021)", "article 188"),
    "10.1136/amiajnl-2011-000089": ("Goddard, K., Roudsari, A., & Wyatt, J. C. (2012)", "121–127"),
    "10.1080/0960085X.2025.2475962": ("Hemmer, P., Schemmer, M., Kühl, N., Vössing, M., & Satzger, G. (2025)", "979–1002"),
    "10.1177/1948550617697177": ("Lakens, D. (2017)", "355–362"),
    "10.1518/hfes.46.1.50_30392": ("Lee, J. D., & See, K. A. (2004)", "50–80"),
    "10.1038/s41583-024-00819-9": ("Silva, A. B., Littlejohn, K. T., Liu, J. R., Moses, D. A., & Chang, E. F. (2024)", "The speech neuroprosthesis"),
    "10.3389/fpsyg.2017.01552": ("Tapal, A., Oren, E., Dar, R., & Eitam, B. (2017)", "article 1552"),
    "10.1038/s41562-024-02024-1": ("Vaccaro, M., Almaatouq, A., & Malone, T. (2024)", "2293–2303"),
}


def bibliography(text: str) -> str:
    section = text.split("## 16.", 1)[1].split("## 17.", 1)[0]
    return "- " + section.split("\n- ", 1)[1].strip()


def main() -> None:
    fr = bibliography(FR.read_text(encoding="utf-8"))
    en = bibliography(EN.read_text(encoding="utf-8"))
    assert fr == en, "FR and EN bibliographies differ"
    for doi, fragments in EXPECTED.items():
        assert fr.count(doi) == 1, doi
        for fragment in fragments:
            assert fragment in fr, (doi, fragment)
    assert "Silva, M." not in fr
    assert "Neurotechnology and neurorights" not in fr
    assert "11 November 2025" in fr
    print(f"PASS: {len(EXPECTED)} DOI records and the UNESCO record match the verified FR/EN bibliography.")


if __name__ == "__main__":
    main()
