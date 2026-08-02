# AI-PlayTest-Skill

Ein allgemeiner Play-Test-Skill für KI-Agenten.

Der Skill hilft dabei, Funktionen aus Sicht echter Nutzerinnen und Nutzer zu testen: lokal, auf Staging oder in einer Live-Umgebung. Er führt den Agenten durch Vorbereitung, Rollenwahl, Testablauf, Notizen, Auswertung, Bugliste, Verbesserungen und Rückbau.

Er ist bewusst allgemein gehalten und kann für Websites, Apps, Admin-Bereiche, Editoren, Spiele, SaaS-Tools, APIs, Shops, interne Tools und andere Softwareprojekte genutzt werden.

## Für wen ist das gedacht?

Für Menschen, die mit KI-Agenten entwickeln und am Ende nicht nur hören wollen: „Tests bestanden“, sondern wissen möchten:

- Kann ein echter Nutzer die Funktion benutzen?
- Versteht ein neuer Nutzer die Oberfläche?
- Funktioniert der Ablauf im Zusammenhang?
- Werden Daten richtig gespeichert und wieder angezeigt?
- Gibt es Sicherheits-, Datenschutz- oder UX-Probleme?
- Was muss nach dem Test verbessert werden?

Der Skill ist für diese Umgebungen formuliert:

- Claude Code (Claude Sonnet 4.6 oder höher; für riskante Live-/Architekturtests Opus 4.8 oder aktueller)
- ChatGPT Codex (GPT-5-Codex oder neuestes Codex-Modell; für lange Live-Tests das stärkste verfügbare Codex-Modell)
- ChatGPT Codex (GPT-5-Codex oder höher)
- ChatGPT Cowork (GPT-5.5 oder aktuelles bestes Reasoning-/Coding-Modell)
- andere agentische Coding- oder QA-Umgebungen, die Markdown-Skills lesen können (bestes verfügbares Coding-/Agentenmodell; für einfache lokale Tests reicht oft ein kleineres schnelles Modell)

## Schnellstart

Kopiere oder klone dieses Repository in den Skill-Ordner deiner Agentenumgebung.

Beispiele:

```bash
# Codex
mkdir -p ~/.codex/skills
git clone https://github.com/MichaelGahnDESIGN/MGD_AI-PlayTest_SKILL.git ~/.codex/skills/playtest

# Claude Code
mkdir -p ~/.claude/skills
git clone https://github.com/MichaelGahnDESIGN/MGD_AI-PlayTest_SKILL.git ~/.claude/skills/playtest
```

Danach kannst du in einem Projekt zum Beispiel schreiben:

```text
/playtest
Teste die neue Registrierungsstrecke aus Sicht eines neuen Nutzers.
```

Oder für eine Live-Umgebung:

```text
/playtest-live
Teste den Admin-Editor live. Erstelle vorher ein Backup, nutze nur temporäre Testdaten und setze am Ende alles zurück.
```

Hinweis: `/playtest` und `/playtest-live` sind Prompt-Konventionen. Ob sie als echte Slash-Commands erscheinen, hängt von deiner Agentenumgebung ab. Der Skill reagiert auch auf normale Formulierungen wie „Mach einen lokalen Play-Test“ oder „Teste das live aus Nutzersicht“.

Dieses Repository enthält zusätzlich Command-Vorlagen:

```text
.claude/commands/playtest.md
.claude/commands/playtest-live.md
.codex/commands/playtest.md
.codex/commands/playtest-live.md
```

Wenn deine Umgebung lokale Command-Dateien unterstützt, können diese Vorlagen dafür sorgen, dass `/playtest` und `/playtest-live` direkter als Befehle verfügbar sind.

## Was macht der Skill?

Der Agent fragt zuerst die wichtigsten Testdaten ab:

- Was soll getestet werden? App, Editor, Website, API, Spiel, Shop, Admin-Bereich oder etwas anderes?
- Lokal, Staging oder Live?
- Aus welcher Rolle? Neuer Nutzer, Admin, Spieler, Kunde, Redakteur, Support, DM, Gast?
- Soll der Agent mehrere Rollen oder Sub-Agenten simulieren?
- Gibt es Testzugänge, Einladungscodes, Testdaten oder spezielle Regeln?
- Welche Funktionen gehören in die Checkliste?
- Welche Risiken gibt es bei Live-Tests?
- Wie werden Testdaten am Ende zurückgebaut?
- Welche Zusatzwerkzeuge sind vorhanden und dürfen genutzt werden?

Dann legt der Agent einen lokalen Play-Test-Ordner an und protokolliert alles dort.

Vor dem Test prüft der Skill außerdem, ob passende Zusatzwerkzeuge vorhanden sind, zum Beispiel Superpowers-Skills, Playwright/Browser-Tools, Caveman-Skills, Sub-Agent-/Multi-Agent-Funktionen, DEV-/Deploy-Skills oder MCP-Server. Der Agent soll sie nicht einfach still nutzen, sondern kurz fragen, welche davon erlaubt sind.

## Ordnerstruktur

Standardmäßig entsteht im Projekt ein Ordner `PLAYTEST/`.

Für jeden Lauf wird ein Unterordner angelegt:

```text
PLAYTEST/
└── Playtest-live_DD-MM-YYYY-1/
    ├── Test-Aufgabe.md
    ├── Test-Protokoll.md
    ├── Test-Auswertung.md
    ├── Test-Bugfix.md
    ├── Test-Todo.md
    ├── Test-Verbesserungsvorschlaege.md
    └── Artefakte/
```

Für lokale Tests heißt der Ordner entsprechend:

```text
PLAYTEST/Playtest-local_DD-MM-YYYY-1/
```

Der Ordner `PLAYTEST/` wird automatisch in `.gitignore` eingetragen. Play-Test-Notizen, Screenshots, temporäre Daten und interne Befunde bleiben dadurch lokal.

## Dateien

`Test-Aufgabe.md`

Beschreibt Ziel, Rolle, Umgebung, Checkliste und Annahmen.

`Test-Protokoll.md`

Enthält den zeitlichen Ablauf: Was wurde geklickt, eingegeben, beobachtet und geprüft?

`Test-Auswertung.md`

Fasst zusammen, was funktioniert hat, was nicht funktioniert hat und wie gut der Ablauf aus Sicht der Testrolle war.

`Test-Bugfix.md`

Listet gefundene Bugs mit Reproduktionsschritten, erwartetem Ergebnis, tatsächlichem Ergebnis, Schweregrad und Vorschlag.

`Test-Todo.md`

Enthält konkrete nächste Aufgaben nach dem Play-Test.

`Test-Verbesserungsvorschlaege.md`

Sammelt UX-, UI-, Sicherheits-, Datenschutz-, Performance- und Produktideen.

`Artefakte/`

Optionaler lokaler Ordner für Screenshots, JSON-Reports, Logs oder Exportdateien. Keine Secrets speichern.

## Live-Tests

Live-Tests sind riskanter als lokale Tests. Deshalb gilt:

- Vor schreibenden Live-Tests muss ein Backup oder ein anderer geprüfter Rückfallpunkt existieren.
- Testdaten müssen klar als temporär erkennbar sein.
- Es muss einen Rückbauplan geben, bevor der Agent produktive Daten ändert.
- Passwörter, Tokens, E-Mail-Inhalte, Zahlungsdaten oder personenbezogene Daten dürfen nicht in die Testdateien geschrieben werden.
- Der Agent prüft am Ende, ob Testdaten wirklich entfernt wurden.
- Wenn kein sicherer Rückbau möglich ist, testet der Agent read-only oder fragt nach Freigabe.

## Beispiel-Prompt

```text
/playtest-live

Teste die Live-Version von [Projektname].

Tu so, als wärst du ein erfahrener Nutzer, der die App zum ersten Mal sieht.
Du willst dich registrieren, ein Profil erstellen, eine Gruppe anlegen, eine Funktion benutzen und danach prüfen, ob alles gespeichert wurde.

Nutze diesen Einladungscode: [TEST-CODE]
Falls Zugangsdaten nötig sind, frage danach oder nutze nur sichere Testzugänge.

Wichtig:
- Erstelle vorher ein Backup, wenn du live schreibst.
- Speichere keine Passwörter oder Tokens in den Play-Test-Dateien.
- Nutze temporäre Testdaten.
- Setze am Ende alles auf den Ursprungszustand zurück.
- Notiere, was funktioniert, was nicht funktioniert und was verbessert werden sollte.
```

## Agenten und Sub-Agenten

Der Skill kann mehrere Rollen simulieren, wenn die Umgebung das unterstützt.

Beispiele:

- Nutzer und Admin
- Käufer und Support
- Spieler, Freunde und Spielleiter
- Redakteur und Reviewer
- Gast und eingeloggter Nutzer

Wenn keine Sub-Agenten verfügbar sind, simuliert der Hauptagent die Rollen nacheinander und dokumentiert die Grenze ausdrücklich.

## Sicherheit und Datenschutz

Der Skill ist so geschrieben, dass Testdaten lokal bleiben.

Er soll niemals:

- echte Passwörter in Markdown-Dateien schreiben,
- Tokens oder Sessiondaten veröffentlichen,
- personenbezogene Daten unnötig kopieren,
- Zahlungsdaten testen, wenn keine Sandbox vorhanden ist,
- produktive Daten ohne Backup und Rückbauplan verändern,
- Screenshots mit sensiblen Daten veröffentlichen.

## Enthaltene Dateien

```text
SKILL.md
scripts/init_playtest.py
README.md
LICENSE
.gitignore
.claude/commands/playtest.md
.claude/commands/playtest-live.md
.codex/commands/playtest.md
.codex/commands/playtest-live.md
docs/wiki/
```

`scripts/init_playtest.py` kann der Agent nutzen, um die Play-Test-Struktur zuverlässig anzulegen.

Parameter:

| Parameter | Standard | Beschreibung |
| --- | --- | --- |
| `--mode` | `local` | `local` oder `live` |
| `--root` | `.` | Projektwurzel |
| `--base` | `PLAYTEST` | Name des Basisordners (z. B. `PlayTest`) |

Beispiel:

```bash
python3 ~/.claude/skills/playtest/scripts/init_playtest.py --mode live --root /pfad/zum/projekt
python3 ~/.codex/skills/playtest/scripts/init_playtest.py --mode live --root /pfad/zum/projekt

# Eigener Basisordner:
python3 ~/.claude/skills/playtest/scripts/init_playtest.py --mode local --root . --base PlayTest
```

## Optionale Kombinationen

Der PlayTest-Skill funktioniert allein. Noch stärker wird er in Kombination mit spezialisierten Skills, MCP-Servern oder Browser-Werkzeugen.

Empfohlen:

- Superpowers-Skills für strukturierte Planung, Test-Driven Development, systematisches Debugging und Verifikation vor Abschluss.
- Playwright oder Browser-Tools für echte UI-Flows, Screenshots, Konsolenfehler, Netzwerkfehler und Regressionstests.
- Caveman-Skills für sehr kompakte Statusmeldungen und knappe Testauswertungen, wenn Kontext gespart werden soll.
- Sub-Agent- oder Multi-Agent-Workflows, wenn mehrere Nutzerrollen simuliert werden sollen.
- Projektinterne DEV-/Deploy-Skills, wenn vor Live-Tests Backup, Restore, Staging oder Deployment geprüft werden müssen.

## Verwandte Projekte Von Michael Gahn DESIGN

Der AI-PlayTest-Skill gehört zu einer kleinen Werkzeugfamilie für
KI-gestützte Projektarbeit.

- [AI-Basic-Projektordner](https://github.com/MichaelGahnDESIGN/MGD_AI-Basic-Projektordner_TOOL)  
  Eine saubere Projektvorlage mit Regeln, Dokumentation, Agentenstruktur und
  Sicherheitsgrenzen. Sinnvoll als Basis für neue Projekte.

- [AI Project Updater Skill](https://github.com/MichaelGahnDESIGN/MGD_AI-Project-Updater_SKILL)  
  Ein geführter Assistent für lokale Staging-Umgebungen, Docker-Planung,
  Update-Vorbereitung und sichere Staging-zu-Live-Abläufe. Das Repository ist
  während der Entwicklung zunächst privat.

- [DEV-Skill](https://github.com/MichaelGahnDESIGN/MGD_DEV_SKILL)  
  Ein projektneutraler Skill für Projekt-Sync, Tests, GitHub-Abgleich,
  Deploy-Vorbereitung, Backups und Abschlussberichte.

- [ProjectClean-Skill](https://github.com/MichaelGahnDESIGN/MGD_ProjectClean_SKILL)  
  Ein Abschluss- und Aufräum-Skill für Versionen, Tests, Commits, Backups,
  Dokumentation und vorsichtiges Cleanup.

- [Claude-Codex-MCP](https://github.com/MichaelGahnDESIGN/MGD_Claude-Codex_MCP)  
  Ein lokales MCP-System für Aufgaben, Chat und Übergaben zwischen Claude,
  Codex und weiteren KI-Agenten.

## Wiki und Beispiele

Ausführliche Beispiele, Checklisten, Live-Test-Regeln, Datenschutz-Hinweise und Troubleshooting findest du im Wiki-Bereich:

- [docs/wiki/Home.md](docs/wiki/Home.md)
- GitHub Wiki: <https://github.com/MichaelGahnDESIGN/MGD_AI-PlayTest_SKILL/wiki>

## Lizenz

MIT Lizenz. Siehe [LICENSE](LICENSE).

## 🔒 Lokal-only — Playtests, Backups & sensible Daten

Diese Daten dürfen **niemals** die lokale Maschine verlassen — weder nach GitHub noch nach Live/Deploy:

- **Playtests:** Play-Test-Branches (`PlayTest*`) und -Artefakte (`PlayTest/`, Protokolle, Screenshots) bleiben lokal.
- **Backups:** DB-Dumps, `*.sql`, `*.sql.gz`, `BACKUPS/` bleiben lokal — nie nach GitHub, nie in den Webroot/Live.
- **Sensible Daten:** `.env*` (außer `.env.example`), Tokens, API-Keys, Passwörter, `*.pem`, `*.key`, Zugangsdaten — niemals committen/pushen/deployen.
- **Push-Disziplin:** Nur den Hauptbranch (`main`) pushen, **niemals** `git push --all`/`--mirror`. `PlayTest*`-Branches werden nie gepusht.

Alle genannten Muster gehören in `.gitignore`. Technische Absicherung: der Pre-Push-Hook aus dem [MGD-DEV-Skill](https://github.com/MichaelGahnDESIGN/MGD_DEV_SKILL) (`dev/hooks/pre-push`) blockiert solche Pushes hart — empfohlen, am besten global via `git config --global core.hooksPath ~/.git-hooks`.

---

## Verwandte MGD Projekte

| Projekt | Beschreibung |
|---------|-------------|
| [MGD-App-Updater-Skill](https://github.com/MichaelGahnDESIGN/MGD_Software-Updater_SKILL) | Software-Update-Systeme planen und implementieren |
| [MGD-Bugreport-Skill](https://github.com/MichaelGahnDESIGN/MGD_BugReport_SKILL) | Feedback-Hub: Bug-Meldung, Ideen und Support |
| [MGD-DEV-Skill](https://github.com/MichaelGahnDESIGN/MGD_DEV_SKILL) | Release, Sync, Backup und Wissensdokumentation |
| [MGD-AI-Basic-Projektordner](https://github.com/MichaelGahnDESIGN/MGD_AI-Basic-Projektordner_TOOL) | Projektvorlage für KI-Agenten |

→ Alle öffentlichen Projekte: [github.com/MichaelGahnDESIGN](https://github.com/MichaelGahnDESIGN)

---

## Impressum

Angaben gemäß § 5 DDG — Siehe [`IMPRESSUM.md`](IMPRESSUM.md).
