<div align="center">

🌐 [Português (BR)](README.pt_BR.md) | [Español](README.es.md)

# 🎉 Soc Ops

### Social Bingo for Real-World Mixers

*Break the ice. Find your people. Get five in a row.*

[![Python](https://img.shields.io/badge/python-3.13%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/license-MIT-22c55e)](LICENSE)
[![Lint](https://img.shields.io/badge/lint-ruff-purple)](https://docs.astral.sh/ruff/)
[![Tests](https://img.shields.io/badge/tests-pytest-blue)](https://docs.pytest.org/)

</div>

---

## ✅ Dev Checklist

Before opening a PR, confirm all three gates pass locally:

```bash
# 1 — Lint
uv run ruff check .

# 2 — Build / type-check
uv run python -c "import app.main"

# 3 — Test
uv run pytest
```

> All three must be green. No exceptions. ✔️

---

## ✨ What Is Soc Ops?

**Soc Ops** turns awkward networking events into something people actually enjoy.  
Players get a personalised 5 × 5 bingo card filled with prompts like *"Has lived in 3+ countries"* or *"Owns a plant they've named"*. Walk around, find real humans who match — mark them off and shout **BINGO!**

```
┌──────────┬──────────┬──────────┬──────────┬──────────┐
│  Speaks  │  Rescue  │  Runs    │ Morning  │  Plays   │
│  2 langs │  pet     │  5K+     │ person   │  guitar  │
├──────────┼──────────┼──────────┼──────────┼──────────┤
│  Remote  │  Loves   │  ★ FREE  │  Reads   │  Hates   │
│  worker  │  sushi   │  SPACE   │  sci-fi  │  Mondays │
├──────────┼──────────┼──────────┼──────────┼──────────┤
│  Lived   │  Night   │  Board   │  Moved   │  Makes   │
│  abroad  │  owl     │  gamer   │  cities  │  memes   │
└──────────┴──────────┴──────────┴──────────┴──────────┘
```

---

## 🔥 Key Features

| Feature | Details |
|---------|---------|
| 🃏 **Random card generation** | Every player gets a unique, shuffled bingo card |
| 👆 **One-tap marking** | HTMX-powered instant updates — no page reload |
| 🏆 **Win detection** | Automatic row / column / diagonal checking |
| 🎊 **Celebration modal** | Confetti burst when you hit bingo |
| 📱 **Mobile-first** | Playable on any phone in the room |
| ⚡ **Zero JS frameworks** | FastAPI + Jinja2 + HTMX — fast and lean |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.13+
- [`uv`](https://docs.astral.sh/uv/) (recommended) **or** plain `pip`

### Fastest Start

```bash
uv sync
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Then open **http://localhost:8000**.

### Run Locally

```bash
# Clone
git clone https://github.com/fbrase-itk/my-soc-ops-python.git
cd my-soc-ops-python

# Install dependencies
uv sync

# Start the dev server
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Run with pip (alternative)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open **http://localhost:8000** — your bingo card is ready. 🎲

---

## 📚 Workshop Lab Guide

This repo is also the foundation for a hands-on GitHub Copilot workshop.  
Work through the parts in order:

| Part | Title | What You'll Do |
|------|-------|----------------|
| [**00**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=00-overview) | Overview & Checklist | Get oriented, validate your environment |
| [**01**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=01-setup) | Setup & Context Engineering | Wire up Copilot context files |
| [**02**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=02-design) | Design-First Frontend | Build the UI with AI assistance |
| [**03**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=03-quiz-master) | Custom Quiz Master | Create a specialised Copilot agent |
| [**04**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=04-multi-agent) | Multi-Agent Development | Orchestrate agents to ship features |

> 📝 All guides are available offline in the [`workshop/`](workshop/) folder.

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) and follow the dev checklist above before submitting a PR.

---

<div align="center">

Made with ☕ and a healthy fear of awkward networking events.

</div>
