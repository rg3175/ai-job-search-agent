
from shared import tools


def test_save_and_get_job(monkeypatch):
    saved_data = []

    def fake_load(filename, default):
        return saved_data.copy()

    def fake_save(filename, data):
        saved_data.clear()
        saved_data.extend(data)

    monkeypatch.setattr(tools, "load_json", fake_load)
    monkeypatch.setattr(tools, "save_json", fake_save)

    job = {
        "id": "123",
        "title": "Full Stack Developer",
        "company": "Test Company",
        "location": "Israel",
        "technologies": ["Python", "React"],
        "url": "https://example.com"
    }

    result = tools.save_job(job)

    assert result["success"] is True
    assert len(tools.get_saved_jobs()["jobs"]) == 1


def test_update_preferences(monkeypatch):
    data = {}

    def fake_load(filename, default):
        return data.copy() if data else default.copy()

    def fake_save(filename, new_data):
        data.update(new_data)

    monkeypatch.setattr(tools, "load_json", fake_load)
    monkeypatch.setattr(tools, "save_json", fake_save)

    result = tools.update_preferences(
        preferred_roles=["Full Stack Developer"],
        technologies=["Python", "Angular"]
    )

    assert result["success"] is True
    assert "Python" in result["preferences"]["technologies"]
