import runpy
import sys
from pathlib import Path
from types import SimpleNamespace


def test_run_starts_uvicorn(monkeypatch):
    from app import main

    calls = {}

    def fake_run(*args, **kwargs):
        calls["args"] = args
        calls["kwargs"] = kwargs

    monkeypatch.setitem(sys.modules, "uvicorn", SimpleNamespace(run=fake_run))

    main.run()

    assert calls["args"] == ("app.main:app",)
    assert calls["kwargs"] == {"host": "0.0.0.0", "port": 8000, "reload": True}


def test_module_execution_starts_uvicorn(monkeypatch):
    calls = {"count": 0}

    def fake_run(*args, **kwargs):
        calls["count"] += 1
        calls["args"] = args
        calls["kwargs"] = kwargs

    monkeypatch.setitem(sys.modules, "uvicorn", SimpleNamespace(run=fake_run))
    main_path = Path(__file__).resolve().parents[1] / "app" / "main.py"
    runpy.run_path(str(main_path), run_name="__main__")

    assert calls["count"] == 1
    assert calls["args"] == ("app.main:app",)
    assert calls["kwargs"] == {"host": "0.0.0.0", "port": 8000, "reload": True}
