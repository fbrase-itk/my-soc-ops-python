---
description: CSS styling practices and reusable classes for this Python/Jinja2 project.
---

# CSS Styling Guide

## Overview
The UI now uses a professional semantic class system in [app/static/css/app.css](app/static/css/app.css), driven by CSS variables.

Primary goal:
- Reuse existing semantic classes and tokens before introducing new ones.
- Keep markup readable and avoid one-off inline styles.

## Core Design Tokens
Defined in :root:
- Surface/background: --bg-0, --bg-1, --bg-2
- Text: --text-0, --text-1, --text-2
- Accent: --accent, --accent-strong, --accent-soft
- State colors: --success*, --warn*
- Structure: --line, --radius-*, --shadow-*

When extending styles, prefer token usage over hard-coded color values.

## Reusable Class Groups

### Shell and layout
- .app-shell
- .start-shell, .game-shell
- .board-stage, .board-grid

### Card and section patterns
- .start-card
- .game-header
- .game-subheader
- .status-banner
- .modal-card, .modal-overlay

### Buttons
- .btn
- .btn-primary
- .btn-ghost
- .btn-lg

### Board states
- .board-cell
- .state-idle
- .state-marked
- .state-winning
- .state-free
- .cell-text, .cell-check

### Accessibility helpers
- .skip-link
- :focus-visible styles for .btn and .board-cell

## Styling Rules
- Do not add inline styles in templates.
- Prefer semantic classes over large utility-class chains.
- Keep animations subtle and purposeful (enter-up/pop-in style).
- Maintain responsive behavior for mobile and desktop.
- Preserve focus-visible and landmark-friendly semantics.

## Where this applies
- [app/templates/base.html](app/templates/base.html)
- [app/templates/home.html](app/templates/home.html)
- [app/templates/components/start_screen.html](app/templates/components/start_screen.html)
- [app/templates/components/game_screen.html](app/templates/components/game_screen.html)
- [app/templates/components/bingo_board.html](app/templates/components/bingo_board.html)
- [app/templates/components/bingo_modal.html](app/templates/components/bingo_modal.html)
- [app/static/css/app.css](app/static/css/app.css)
