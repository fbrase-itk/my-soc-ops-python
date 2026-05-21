# Copilot Workspace Instructions

## Mandatory Development Checklist

Before marking work as complete, all items must pass:

- [ ] `uv run ruff check .`
- [ ] `uv run python -c "import app.main"`
- [ ] `uv run pytest`

## Project Overview

**Soc Ops** is a Social Bingo game built with Python (FastAPI + Jinja2 + HTMX).
Players find people who match prompts on a 5x5 board and complete a line to win.

## Architecture

```
app/
├── templates/       # Jinja2 templates
│   ├── base.html
│   ├── home.html
│   └── components/  # start_screen, game_screen, bingo_board, bingo_modal
├── static/
│   ├── css/app.css  # Design system + semantic classes
│   └── js/htmx.min.js
├── models.py        # Pydantic models and state enums
├── game_logic.py    # Board generation and bingo detection
├── game_service.py  # Session state management
├── data.py          # Prompt/question bank
└── main.py          # FastAPI routes + HTMX endpoints
tests/
├── test_api.py
└── test_game_logic.py
```

## Key Commands

```bash
uv sync
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
uv run ruff check .
uv run pytest
```

## Design Guide

Use this section whenever you change templates or styles.

- Visual direction: professional, minimal-tech, clean information hierarchy.
- Typography: use the existing IBM Plex Sans setup in `app/templates/base.html`; do not switch to generic default stacks.
- Tokens first: prefer CSS variables in `app/static/css/app.css` (`--bg-*`, `--text-*`, `--accent*`, `--radius-*`, `--shadow-*`) over hard-coded values.
- Semantic classes over long utility chains: favor reusable classes like `.start-card`, `.game-header`, `.board-cell`, `.modal-card`, `.btn-*`.
- Interaction states are required: preserve hover/active/focus-visible behavior for buttons and board cells.
- Accessibility baseline is mandatory: keep skip-link, focus-visible outlines, semantic landmarks, and dialog roles/labels.
- Motion style: subtle and purposeful only (`enter-up`, `pop-in`), avoid flashy or excessive animation.
- Responsive behavior: preserve mobile and desktop layouts, especially board readability and touch targets.
- HTMX boundary: keep server-rendered partial updates (`#game-container` outerHTML swap); do not introduce client-side state frameworks.

## State Management

- `GameSession` manages game state on the server.
- Session state persists via signed cookies.
- UI updates are delivered through HTMX template partials.
