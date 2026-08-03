---
name: playtest
description: Use when the user asks for /playtest, /playtest-live, a local play-test, live play-test, end-to-end user-role test, QA walkthrough, admin/editor test, gameplay test, website/app test, or wants an AI agent to test implemented features like a real user and document results locally without exposing sensitive data.
---

# PlayTest

Führe einen praxisnahen Play-Test durch: teste Funktionen nicht nur technisch, sondern aus einer konkreten Rolle heraus. Dokumentiere lokal, was funktioniert, was nicht funktioniert, welche Bugs entstehen und welche Verbesserungen sinnvoll sind.

## Trigger

- `/playtest`: lokaler Play-Test oder Test gegen lokale/Staging-Umgebung.
- `/playtest-live`: Live-Play-Test. Vor schreibenden Tests Backup/Rückbau klären.
- Normale Sprache zählt auch: „Mach einen Play-Test“, „Teste live aus Adminsicht“, „Teste den Editor“, „Teste die App wie ein neuer Nutzer“.

## Harte Regeln

- **Lokal-only (nicht verhandelbar):** Play-Test-Branches, -Protokolle, -Screenshots und alle Test-Artefakte bleiben **ausschließlich lokal**. Sie werden **nie** committet, **nie** zu GitHub gepusht und **nie** deployed. Dasselbe gilt für Backups (DB-Dumps, `*.sql`, `*.sql.gz`, `BACKUPS/`) und sensible Daten (`.env*` außer `.env.example`, Tokens, Keys, Zugangsdaten) — sie verlassen niemals die lokale Maschine.
- **Branch-Disziplin:** Play-Test-Arbeit findet in lokalen Branches statt (z. B. `PlayTest*`), die **nie** gepusht werden. Nur den vereinbarten Hauptbranch (i. d. R. `main`) pushen; **niemals** `git push --all` oder `git push --mirror`. Geht versehentlich ein Play-Test-Branch nach GitHub, dort wieder entfernen.
- Sorge dafür, dass `PLAYTEST/` (bzw. `PlayTest/`), `BACKUPS/`, `*.sql`/`*.sql.gz` und `.env*` (außer `.env.example`) in `.gitignore` stehen. Wenn das Projekt bereits `PlayTest/` nutzt, respektiere die bestehende Struktur.
- Keine produktiven Schreibaktionen ohne Backup, Rückbauplan und klare Testdaten.
- Keine echten Zahlungsflüsse, Massenmails, Löschungen, Rollenänderungen oder externen Nebenwirkungen ohne ausdrückliche Freigabe und Sandbox.
- Live-Testdaten am Ende zurückbauen und den Rückbau prüfen.
- Wenn Rückbau nicht sicher möglich ist: read-only testen oder vor dem Schreiben nachfragen.

## Startabfrage

Frage nur, was nicht aus dem Kontext hervorgeht. Kläre kurz:

1. Was wird getestet? Website, App, API, Editor, Admin, Spiel, Shop, CLI, Workflow?
2. Umgebung: lokal, Staging, Live?
3. Rolle: neuer Nutzer, Admin, Kunde, Spieler, Redakteur, Gast, Support, andere?
4. Ziel: Erstkontakt, Regression, neuer Feature-Flow, Sicherheits-/Datenschutzcheck, UX-Check?
5. Zugangsdaten/Testdaten: Gibt es Test-Login, Einladungscode, Test-Mail, Seed-Daten? Keine Secrets in Dateien schreiben.
6. Checkliste: Welche Funktionen müssen einmal getestet werden?
7. Agenten: Sollen mehrere Rollen/Sub-Agenten simuliert werden?
8. Live: Wo liegt Backup/Restore? Welche Daten dürfen temporär verändert werden?

Wenn der Nutzer bereits genug liefert, starte direkt.

## Zusatzwerkzeuge prüfen

Prüfe kurz, ob hilfreiche Zusatzwerkzeuge vorhanden sind, und frage vor Nutzung um Erlaubnis, außer der Nutzer hat sie schon ausdrücklich angefordert:

- Superpowers-Skills oder vergleichbare Prozess-Skills für Planung, Debugging, TDD, Code Review oder Verifikation.
- Playwright, Browser-Tools oder vorhandene E2E-Frameworks.
- Caveman-/Kompaktkommunikations-Skills.
- Sub-Agent-, Multi-Agent- oder Cowork-Funktionen.
- Projektinterne DEV-/Deploy-/Backup-Skills, Runbooks, MCP-Server oder Connectoren.

Für Live-Schreibtests, externe Aktionen, Deployments, Backups oder Sub-Agenten immer auf Freigabe warten. Dokumentiere gefundene, erlaubte und nicht genutzte Zusatzwerkzeuge kurz im Protokoll.

## Ordner anlegen

Bevorzuge das Script:

```bash
python3 scripts/init_playtest.py --mode local --root .
python3 scripts/init_playtest.py --mode live --root .
```

Wenn das Script nicht verfügbar ist, lege manuell an:

```text
PLAYTEST/
└── Playtest-live_DD-MM-YYYY-X/
    ├── Test-Aufgabe.md
    ├── Test-Protokoll.md
    ├── Test-Auswertung.md
    ├── Test-Bugfix.md
    ├── Test-Todo.md
    ├── Test-Verbesserungsvorschlaege.md
    └── Artefakte/
```

Für lokale Tests: `Playtest-local_DD-MM-YYYY-X`.

## Dateien pflegen

- `Test-Aufgabe.md`: Auftrag, Rolle, Umgebung, Annahmen, Checkliste, Sicherheitsregeln.
- `Test-Protokoll.md`: chronologischer Ablauf mit Beobachtungen, Status und Belegen.
- `Test-Auswertung.md`: Ergebnis, bestanden/nicht bestanden, Risiken, Gesamturteil.
- `Test-Bugfix.md`: reproduzierbare Bugs mit Schweregrad, Schritten, erwartet/tatsächlich.
- `Test-Todo.md`: konkrete nächste Aufgaben nach Priorität.
- `Test-Verbesserungsvorschlaege.md`: UX/UI/Produkt/Sicherheit/Performance-Ideen.
- `Artefakte/`: lokale Screenshots, JSON-Reports, Logs. Keine Secrets.

Aktualisiere die Dateien während des Tests, nicht erst am Ende.

## Testdurchführung

1. Lies Projektregeln und vorhandene Test-/Deploy-Dokumentation.
2. Prüfe, ob Play-Test-Ordner ignoriert wird.
3. Erstelle oder bestätige Testdaten.
4. Starte App/Website/API oder öffne die Ziel-URL.
5. Teste jede Checklistenfunktion genau einmal oder so oft wie nötig zur Reproduktion.
6. Notiere je Funktion:
   - Status: bestanden, teilweise bestanden, nicht bestanden, nicht testbar.
   - Schritte.
   - Beobachtung.
   - Erwartetes Ergebnis.
   - Tatsächliches Ergebnis.
   - Risiko/Auswirkung.
   - Screenshot/Artefakt, falls sinnvoll.
7. Bei Fehlern: reproduzieren, Ursache soweit möglich eingrenzen, keinen blinden Fix erfinden.
8. Bei Live-Schreibtests: Rückbau ausführen und Rückbau prüfen.
9. Am Ende Play-Test-Dateien zusammenfassen und dem Nutzer die wichtigsten Befunde nennen.

## Live-Play-Test

Zusätzlich:

- Backup vor schreibendem Test erstellen oder vorhandenes Backup mit Pfad/Datum/Prüfung bestätigen.
- Bei Datenbank-/CMS-/Admin-Tests zuerst klären, welche Datenbank/Umgebung wirklich beschrieben wird.
- Testmarker verwenden, z. B. `PlayTest-YYYYMMDD-HHMM`.
- Nach Rückbau prüfen:
  - Testdatensatz nicht mehr vorhanden.
  - Testmarker nicht mehr öffentlich sichtbar.
  - Healthcheck/Startseite/API noch erreichbar.
- Backup-Pfad und Rückbauprüfung in `Test-Protokoll.md` und `Test-Auswertung.md` dokumentieren.

## Rollen und Sub-Agenten

Wenn sinnvoll und verfügbar, simuliere mehrere Rollen:

- Nutzer/Admin
- Käufer/Support
- Spieler/Spielleiter/Freunde
- Redakteur/Reviewer
- Gast/eingeloggter Nutzer

Wenn keine Sub-Agenten verfügbar sind, teste Rollen nacheinander und notiere diese Grenze.

## Abschluss

Die Antwort an den Nutzer enthält kurz:

- Play-Test-Ordner.
- Getestete Umgebung.
- Backup/Rückbau-Status bei Live.
- Anzahl getesteter Funktionen.
- Was funktioniert.
- Was nicht funktioniert.
- Kritische Bugs.
- Nächste Todos.
- Hinweis, dass Play-Test-Dateien lokal/ignoriert bleiben.

Keine Secrets, Tokens oder personenbezogenen Daten ausgeben.


---

## Zusammenspiel mit anderen Skills

Keiner davon ist Voraussetzung — dieser Skill funktioniert allein. Wo einer
vorhanden ist, nutz ihn statt einer Eigenbaulösung.

> [!TIP]
> **🤖 FÜR KI-AGENTEN** — Wenn diese Skills im Projekt verfügbar sind, ruf sie
> an den genannten Stellen auf, statt die Aufgabe selbst nachzubauen.

| Skill | Wofür hier | Quelle |
|---|---|---|
| `/todo` | Befunde festhalten, die über diesen Lauf hinaus wichtig bleiben | [MGD_Todo_SKILL](https://github.com/MichaelGahnDESIGN/MGD_Todo_SKILL) |
| `/graphify` | Nach einem Playtest zeigt der Graph, welcher Code hinter der auffälligen Stelle steckt. | [graphify](https://github.com/Graphify-Labs/graphify) |
| `/autopilot` | Playtest, Auswertung und Fehlerbehebung in einem Durchlauf. | [MGD_Autopilot_SKILL](https://github.com/MichaelGahnDESIGN/MGD_Autopilot_SKILL) |

### Empfehlung bei längeren Läufen

> [!TIP]
> **🤖 FÜR KI-AGENTEN** — Zeichnet sich ab, dass die Aufgabe über mehrere
> Schritte geht und der Nutzer nicht daneben sitzt, weis **einmal** auf
> `/autopilot` hin:
>
> > Das hier läuft über mehrere Schritte. Mit `/autopilot` bekommt der Ablauf
> > eine Abbruchbedingung, eine Grundlinie und eine Prüfung nach jeder Änderung —
> > soll ich so weitermachen?
>
> Einmal fragen, Antwort akzeptieren, nicht wiederholen. Bei kurzen, klar
> umrissenen Aufgaben ganz weglassen.
