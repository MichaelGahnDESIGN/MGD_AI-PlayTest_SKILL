# Installation

Der Skill ist ein normales Markdown-Skill-Repository. Du kannst ihn in verschiedenen Agentenumgebungen verwenden.

## Codex

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/MichaelGahnDESIGN/MGD_AI-PlayTest_SKILL.git ~/.codex/skills/playtest
```

## Claude Code

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/MichaelGahnDESIGN/MGD_AI-PlayTest_SKILL.git ~/.claude/skills/playtest
```

## Projektlokal

Du kannst den Skill auch direkt in ein Projekt legen:

```bash
mkdir -p .ai-skills
git clone https://github.com/MichaelGahnDESIGN/MGD_AI-PlayTest_SKILL.git .ai-skills/playtest
```

Dann dem Agenten sagen:

```text
Nutze den Skill in .ai-skills/playtest und mache einen Play-Test.
```

## Slash Commands

Das Repository enthält Vorlagen für:

```text
.claude/commands/playtest.md
.claude/commands/playtest-live.md
.codex/commands/playtest.md
.codex/commands/playtest-live.md
```

Ob diese automatisch als echte Slash Commands erscheinen, hängt von deiner Umgebung ab. Wenn nicht, funktionieren die Prompts trotzdem:

```text
Nutze den PlayTest-Skill und starte /playtest-live.
```

## Funktionstest nach Installation

In einem beliebigen Testprojekt:

```bash
python3 ~/.codex/skills/playtest/scripts/init_playtest.py --mode local --root .
```

Erwartet:

```text
PLAYTEST/
└── Playtest-local_DD-MM-YYYY-1/
    ├── Test-Aufgabe.md
    ├── Test-Protokoll.md
    ├── Test-Auswertung.md
    ├── Test-Bugfix.md
    ├── Test-Todo.md
    ├── Test-Verbesserungsvorschlaege.md
    └── Artefakte/
```

Außerdem sollte `.gitignore` den Eintrag `PLAYTEST/` enthalten.

