#!/usr/bin/env python3
"""Create a local PLAYTEST folder with standard markdown files.

The script is intentionally dependency-free so AI agents can use it in most
repositories. It never writes secrets and it makes sure PLAYTEST/ is ignored by
Git when a .gitignore file exists or can be created.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


FILES = {
    "Test-Aufgabe.md": """# Test-Aufgabe

## Kontext

- Datum:
- Umgebung:
- Rolle:
- Ziel:

## Sicherheitsregeln

- Keine Passwörter, Tokens, Sessiondaten, Zahlungsdaten oder personenbezogenen Daten speichern.
- Testdaten klar als temporär markieren.
- Bei Live-Tests Backup und Rückbau dokumentieren.

## Checkliste

- [ ] Funktion 1
- [ ] Funktion 2
- [ ] Funktion 3

## Annahmen und Grenzen

- 
""",
    "Test-Protokoll.md": """# Test-Protokoll

## Ablauf

| Zeit | Schritt | Beobachtung | Status |
| --- | --- | --- | --- |

## Belege

- 
""",
    "Test-Auswertung.md": """# Test-Auswertung

## Gesamturteil

- Status:
- Kurzfazit:

## Funktioniert

- 

## Funktioniert nicht oder nur teilweise

- 

## Risiken

- 

## Rückbauprüfung

- Nur für Live-Tests ausfüllen.
""",
    "Test-Bugfix.md": """# Test-Bugfix

## Bugs

### BUG-001: Titel

- Bereich:
- Schweregrad:
- Schritte zur Reproduktion:
- Erwartetes Ergebnis:
- Tatsächliches Ergebnis:
- Auswirkung:
- Vorschlag:
- Status:
""",
    "Test-Todo.md": """# Test-Todo

## Offen

- [ ]

## Erledigt

- [x]
""",
    "Test-Verbesserungsvorschlaege.md": """# Test-Verbesserungsvorschläge

## Hoch

- 

## Mittel

- 

## Niedrig

- 
""",
}


def next_run_dir(base: Path, mode: str, now: datetime) -> Path:
    date = now.strftime("%d-%m-%Y")
    prefix = f"Playtest-{mode}_{date}"
    index = 1
    while True:
        candidate = base / f"{prefix}-{index}"
        if not candidate.exists():
            return candidate
        index += 1


def ensure_gitignore(root: Path, base: str = "PLAYTEST") -> bool:
    """Traegt den Play-Test-Ordner in die .gitignore ein.

    `base` MUSS uebergeben werden, sobald --base benutzt wird. Vorher war der
    Eintrag fest auf "PLAYTEST/" verdrahtet: Wer mit --base einen anderen
    Ordner waehlte, bekam ihn angelegt, aber .gitignore schuetzte ihn nicht --
    die Play-Test-Daten waren damit committbar.
    """
    entry = f"{base.strip('/')}/"
    gitignore = root / ".gitignore"
    existing = gitignore.read_text(encoding="utf-8") if gitignore.exists() else ""
    lines = existing.splitlines()
    if entry in lines:
        return False
    suffix = "" if existing.endswith("\n") or existing == "" else "\n"
    gitignore.write_text(f"{existing}{suffix}{entry}\n", encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a PLAYTEST run folder.")
    parser.add_argument("--mode", choices=["local", "live"], default="local")
    parser.add_argument("--root", default=".", help="Project root")
    parser.add_argument("--base", default="PLAYTEST", help="Play-test base folder")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    base = root / args.base
    base.mkdir(parents=True, exist_ok=True)
    run_dir = next_run_dir(base, args.mode, datetime.now())
    run_dir.mkdir(parents=True)
    artefacts = run_dir / "Artefakte"
    artefacts.mkdir()

    for filename, content in FILES.items():
        (run_dir / filename).write_text(content, encoding="utf-8")

    gitignore_changed = ensure_gitignore(root, args.base)

    result = {
        "mode": args.mode,
        "root": str(root),
        "run_dir": str(run_dir),
        "artefacts_dir": str(artefacts),
        "gitignore_changed": gitignore_changed,
        "files": sorted(FILES.keys()),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
