import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


class TestScavengerModeEntry:
    def test_home_offers_scavenger_hunt_start(self, client: TestClient):
        response = client.get("/")
        assert response.status_code == 200
        assert "Scavenger Hunt" in response.text
        assert 'hx-post="/start-hunt"' in response.text


class TestStartHunt:
    def test_start_hunt_renders_checklist(self, client: TestClient):
        client.get("/")
        response = client.post("/start-hunt")
        assert response.status_code == 200
        assert "Scavenger Hunt" in response.text
        assert "checklist" in response.text.lower()
        assert 'type="checkbox"' in response.text

    def test_start_hunt_uses_list_layout_not_bingo_grid(self, client: TestClient):
        client.get("/")
        response = client.post("/start-hunt")
        assert response.status_code == 200
        assert 'aria-label="Scavenger checklist"' in response.text
        assert 'class="board-grid"' not in response.text
        assert "FREE SPACE" not in response.text

    def test_start_hunt_shows_progress_meter(self, client: TestClient):
        client.get("/")
        response = client.post("/start-hunt")
        assert response.status_code == 200
        assert "Progress" in response.text
        assert "0 /" in response.text


class TestScavengerProgress:
    def test_toggle_in_hunt_mode_updates_progress(self, client: TestClient):
        client.get("/")
        start = client.post("/start-hunt")
        assert start.status_code == 200
        assert "0 /" in start.text

        toggled = client.post("/toggle/0")
        assert toggled.status_code == 200
        assert "1 /" in toggled.text

    def test_completing_hunt_shows_completion_state(self, client: TestClient):
        client.get("/")
        start = client.post("/start-hunt")
        assert start.status_code == 200

        # The hunt should expose checkbox toggles.
        # Marking all should show a completion message.
        for square_id in range(24):
            client.post(f"/toggle/{square_id}")

        completed = client.post("/toggle/24")
        assert completed.status_code == 200
        assert "Scavenger Hunt complete" in completed.text
