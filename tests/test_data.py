from app.data import QUESTIONS


def test_tech_life_question_pool_size():
    assert len(QUESTIONS) >= 24


def test_tech_life_themes_present():
    assert "has strong opinions about tabs vs spaces" in QUESTIONS
    assert "customized their IDE theme beyond recognition" in QUESTIONS
    assert "has debated semicolons in at least one code review" in QUESTIONS
